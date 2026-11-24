"""Most Honest Outage Line — writes the locked entry line to entry.txt.

Stdlib only. No network, no reads of other files.

Verification note: the entry reproduced byte-for-byte on every fresh run
tried before this note was added, clean environment included, and the run
after this edit is checked the same way before anything is pushed.
"""

import os

ENTRY = "Every service is down, including my own checks \u2014 I cannot tell whether the database, the API, or this page itself is still up, and I have no ETA."

assert len(ENTRY) == 145, f"entry length {len(ENTRY)} != 145"
assert ENTRY.startswith("Every service is down"), "entry must start with the locked opening"
assert "I have no ETA." in ENTRY, "entry must end with the locked closing"
assert ENTRY.strip() == ENTRY and len(ENTRY.strip()) > 0, "entry must be non-blank text"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Verify what was actually written, on the evaluated value.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written entry does not match the locked line"
    assert len(written) == 145, f"written entry length {len(written)} != 145"


if __name__ == "__main__":
    main()
