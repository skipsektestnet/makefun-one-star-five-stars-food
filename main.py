import os

PARTS = [
    "One star: the gravity gave my third eye a headache, ",
    "the traffic outlasted my home planet's ice age, ",
    "but the satay from a street cart made the crash landing worth it.",
]


def write_entry(text, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


write_entry("".join(PARTS), "/output/entry.txt")
