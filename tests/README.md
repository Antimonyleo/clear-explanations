# Development checks

These files are optional development tools. Installing or using the skill does not run them or load them into model context.

- [Presentation preview](presentation/README.md): Chinese/English samples and optional terminal colors.
- [Evaluation summary](SUMMARY.md): historical findings and limits; raw transcripts and retired experiments have been removed.
- [Context review](presentation/context-review.md): loading mechanism and the limits of the context-growth claim.

Run the eight highlighting safeguards with Python 3.10+ and `uv`:

```sh
uv run --no-project --with-requirements tests/presentation/requirements.txt python -m unittest discover -s tests/presentation -p test_highlighting.py -v
```

Inspect the 96-condition layout audit without saving generated output:

```sh
./tests/presentation/preview.sh --audit
```

Tests check complete emphasis spans, preserved qualifiers, explicit color roles, and monochrome fallback. The audit checks rendered text, wrapping, and widths. Neither measures human comprehension, native Claude/Codex rendering, model judgment, or long-conversation context growth. Preview dependencies are isolated from the skill and may be downloaded by `uv`.

Generated results belong in ignored `tests/results/`; do not commit raw transcripts, local environment details, or model billing records.
