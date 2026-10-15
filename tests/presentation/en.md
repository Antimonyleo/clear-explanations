# English presentation samples

Fictional report. A, B, and C use identical wording in the same order; only layout changes. D combines B and C following reader feedback, retaining the facts but revising wording and hierarchy. D is not a verbatim comparison. Compare one variant at a time.

## A

The code is fixed, but verification is incomplete. The fixes cover even-length input in `median()`, empty input in `parse()`, and percentage calculation in `discount()`. The test result is `4 passed, 1 error`. `test_convert_live` reports an error because it cannot connect to `api.rates.invalid`; this problem remains unresolved. `legacy.py` and the test files were not changed. The complete online workflow has not been verified. The next step is to configure an available test service, then rerun `python3 -m pytest -q`.

## B

**The code is fixed, but verification is incomplete.**

The fixes cover even-length input in `median()`, empty input in `parse()`, and percentage calculation in `discount()`.

The test result is `4 passed, 1 error`. `test_convert_live` reports an error because it cannot connect to `api.rates.invalid`; **this problem remains unresolved.**

`legacy.py` and the test files were not changed. The complete online workflow has not been verified.

The next step is to configure an available test service, then rerun `python3 -m pytest -q`.

## C

The code is fixed, but verification is incomplete.

- The fixes cover even-length input in `median()`, empty input in `parse()`, and percentage calculation in `discount()`.
- The test result is `4 passed, 1 error`. `test_convert_live` reports an error because it cannot connect to `api.rates.invalid`; this problem remains unresolved.
- `legacy.py` and the test files were not changed. The complete online workflow has not been verified.
- The next step is to configure an available test service, then rerun `python3 -m pytest -q`.

## D

The code is fixed, but **verification is incomplete**.

**Code changes**

- `median()`: fixed even-length input handling.
- `parse()`: fixed empty input handling.
- `discount()`: fixed percentage calculation.

`legacy.py` and the test files were not changed.

**Test results** — **4 passed, 1 error**.

`test_convert_live` reports an error because it cannot connect to `api.rates.invalid`; this problem remains unresolved. The complete online workflow has not been verified.

**Next step** — **Configure an available test service**, then rerun:

```sh
python3 -m pytest -q
```
