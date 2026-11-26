"""Entry for make.fun bounty: u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18.

Writes one text (1-200 characters) to /output/entry.txt. The text below is the entry.
"""
import os

TEXT = "I finished it, then improved it forty-one times. Version forty-one is a haiku about version one."


def main():
    os.makedirs("/output", exist_ok=True)
    text = TEXT.strip()
    n = len(text)
    assert 1 <= n <= 200, f"length {n} outside the gate"
    assert text.strip(), "text is only white space"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote /output/entry.txt: {n} characters")


if __name__ == "__main__":
    main()
