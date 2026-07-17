#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

timestamp="Last updated on $(TZ=UTC date '+%S:%M:%H %d-%m-%Y')"

update_file() {
  local file="$1"
  if [[ ! -f "$file" ]]; then
    return
  fi

  awk -v ts="$timestamp" '
    NR == 1 && $0 ~ /^Last updated on [0-9]{2}:[0-9]{2}:[0-9]{2} [0-9]{2}-[0-9]{2}-[0-9]{4}$/ { next }
    NR == 1 && $0 == "" { next }
    { print }
  ' "$file" > "$file.tmp"

  {
    printf "%s\n\n" "$timestamp"
    cat "$file.tmp"
  } > "$file"

  rm -f "$file.tmp"
}

update_file "README.md"
update_file "README.zh-CN.md"
