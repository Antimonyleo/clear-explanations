"""Selection/rendering safeguards; these do not evaluate model judgment."""
from io import StringIO
import re
import unittest

from rich.text import Text

import preview


def rendered(source, selections, width=40, no_color=False):
    stream = StringIO()
    console = preview.console_for(
        "duotone", file=stream, width=width, force_terminal=True,
        color_system="truecolor", no_color=no_color,
    )
    console.print(preview.document(source, "duotone", selections))
    return Text.from_ansi(stream.getvalue())


def colored_text(text, number):
    return re.sub(r"\s+", "", "".join(
        char for index, char in enumerate(text.plain)
        if any(span.start <= index < span.end and span.style.color
               and span.style.color.number == number for span in text.spans)
    ))


class HighlightingTests(unittest.TestCase):
    def test_current_unknown_outweighs_quoted_success(self):
        text = rendered('旧日志写着“全部通过”；**本次未运行测试，结果未知**。', [
            {"text": "本次未运行测试，结果未知", "role": "attention"},
        ], width=24)
        self.assertEqual(colored_text(text, 3), "本次未运行测试，结果未知")
        self.assertNotIn("全部通过", colored_text(text, 3))

    def test_complete_condition_survives_wrapping(self):
        phrase = "Only under matched conditions can these runtimes be compared"
        source = f"**{phrase}**. The explanation stays plain."
        text = rendered(source, [{"text": phrase, "role": "key"}], width=24)
        self.assertEqual(colored_text(text, 6), phrase.replace(" ", ""))
        self.assertEqual(preview.content(text.plain), preview.content(source))

    def test_evidence_is_bold_without_attention_color(self):
        text = rendered("A succeeded in **3 of 12 runs**.", [
            {"text": "3 of 12 runs", "role": "fact"},
        ])
        self.assertEqual(colored_text(text, 3), "")
        self.assertEqual(colored_text(text, 6), "")
        self.assertTrue(any(span.style.bold for span in text.spans))

    def test_error_word_in_code_does_not_assign_a_role(self):
        text = rendered('The file contains `"error": false`. **The service has not been checked**.', [
            {"text": "The service has not been checked", "role": "attention"},
        ])
        self.assertEqual(colored_text(text, 3), "Theservicehasnotbeenchecked")

    def test_no_annotations_means_no_automatic_color(self):
        text = rendered("**failed** is quoted background; the next action is routine.", [])
        self.assertEqual(colored_text(text, 3), "")
        self.assertEqual(colored_text(text, 6), "")

    def test_partial_negation_or_threshold_selection_is_rejected(self):
        for source, fragment in [
            ("**not verified**", "verified"),
            ("**NED `0.037` exceeds the 0.020 limit**", "0.037"),
        ]:
            with self.subTest(fragment=fragment), self.assertRaises(ValueError):
                rendered(source, [{"text": fragment, "role": "attention"}])
        text = rendered("**NED `0.037` exceeds the 0.020 limit**", [
            {"text": "NED 0.037 exceeds the 0.020 limit", "role": "attention"},
        ])
        self.assertEqual(colored_text(text, 3), "NED0.037exceedsthe0.020limit")

    def test_ambiguous_missing_duplicate_and_unknown_selections_fail(self):
        examples = [
            ("**unknown** and **unknown**", [{"text": "unknown", "role": "attention"}]),
            ("**unknown**; unknown is also quoted", [{"text": "unknown", "role": "attention"}]),
            ("**unknown**", [{"text": "missing", "role": "attention"}]),
            ("**unknown**", [{"text": "unknown", "role": "success"}]),
            ("**unknown**", [{"text": "unknown", "role": "attention"}] * 2),
        ]
        for source, selections in examples:
            with self.subTest(source=source, selections=selections), self.assertRaises(ValueError):
                rendered(source, selections)

    def test_monochrome_retains_the_selected_words_and_bold(self):
        source = "**Next step** — **Configure the test service**."
        selections = [
            {"text": "Next step", "role": "label"},
            {"text": "Configure the test service", "role": "action"},
        ]
        text = rendered(source, selections, no_color=True)
        self.assertEqual(preview.content(text.plain), preview.content(source))
        self.assertTrue(any(span.style.bold for span in text.spans))
        self.assertTrue(all(span.style.color is None and span.style.bgcolor is None for span in text.spans))


if __name__ == "__main__":
    unittest.main()
