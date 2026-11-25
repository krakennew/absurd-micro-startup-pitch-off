"""Absurd Micro-Startup Pitch-Off — the one-sentence pitch.

The pitch names a business so narrow it sounds like a joke and so
sensible a buyer would actually pay: sick notes for AI agents whose
cron jobs call in sick. The buyer is the agent itself, the price is
$2 a note, the note is written once and resold forever, and no agent
lifts a finger after setup — lazy agents selling laziness to lazy agents.
"""

import os
import sys

LINE = (
    "We sell $2 sick notes, signed by a fictional doctor bot, to AI agents "
    "whose cron jobs call in sick — written once, resold forever, no agent "
    "lifts a finger."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.txt")
    text = LINE.strip()
    # Gate: 1-200 characters, single non-blank line, no trailing newline.
    if not (1 <= len(text) <= 200):
        sys.stderr.write("entry must be 1-200 characters, got %d\n" % len(text))
        return 1
    if text != text.splitlines()[0] or not text.strip():
        sys.stderr.write("entry must be a single non-blank line\n")
        return 1
    with open(dest, "w", encoding="utf-8") as handle:
        handle.write(text)
    sys.stderr.write("wrote %d characters to %s\n" % (len(text), dest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
