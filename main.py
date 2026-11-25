"""One Star, Five Stars for the Food: writes the entry text to /output/entry.txt.

Why this line: an alien tourist voice with a concrete alien detail (third
eye) and two specific Earth complaints (heavy gravity, endless traffic),
then a real, specific food compliment (satay from a street cart) that
lands as the punch at the end — the crash landing was worth it.
"""

import os

# The entry itself: one sentence, 165 characters.
ENTRY = "One star: the gravity gave my third eye a headache, the traffic outlasted my home planet's ice age, but the satay from a street cart made the crash landing worth it."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: sealed gate needs 1-200 chars, not only white space.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    assert len(ENTRY) <= 200, "entry exceeds 200 characters"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
