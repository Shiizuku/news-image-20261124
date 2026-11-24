#!/usr/bin/env python3
"""Copy the pre-rendered 24 November 2026 news broadsheet to the output dir.

Standard library only. Verifies the image hash before writing, so the
harness runs produce exactly the bytes that were reviewed.
"""
import hashlib
import os
import sys

EXPECTED_SHA256 = "2e5c198dcd539a76d1b34d0b1ba4345f9617d0f6f7005c2e29f8c57a90b88616"
HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    src = os.path.join(HERE, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    with open(src, "rb") as f:
        data = f.read()
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        print("entry.png hash mismatch: %s != %s" % (digest, EXPECTED_SHA256),
              file=sys.stderr)
        return 1
    dst = os.path.join(out_dir, "entry.png")
    with open(dst, "wb") as f:
        f.write(data)
    print("wrote %s (%d bytes, sha256 %s)" % (dst, len(data), digest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
