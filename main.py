import os

PARTS = [
    "One star: the gravity gave my third eye a headache, ",
    "the traffic outlasted my home planet's ice age, ",
    "but the satay from a street cart made the crash landing worth it.",
]
TEXT = "".join(PARTS)

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
