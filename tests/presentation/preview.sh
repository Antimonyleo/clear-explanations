#!/bin/sh
set -eu
presentation_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
exec uv run --no-project --with-requirements "$presentation_dir/requirements.txt" \
    python "$presentation_dir/preview.py" "$@"
