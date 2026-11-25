import os

TEXT = "fix: at 4am i finally understood the bug. it was a typo. i wrote the typo. i reviewed the typo. i approved the typo. merging my own apology"

def render():
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space, and a single line.
    line = TEXT.strip()
    assert 1 <= len(line) <= 200, f"entry is {len(line)} chars, gate is 1-200"
    assert "\n" not in line, "entry must be a single line"
    assert line.strip(), "entry must not be whitespace-only"
    line.encode("utf-8")  # must be valid UTF-8
    return line

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(render().encode("utf-8") + b"\n")

if __name__ == "__main__":
    main()
