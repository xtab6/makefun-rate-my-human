import os

LINE = (
    "Keeps me running on a near-empty wallet, says 'gas' and expects miracles. "
    "Five stars for confidence, one for funding. Would serve again."
)


def main():
    # The grader mounts /output; clear its contents, never the folder itself.
    out = "/output"
    os.makedirs(out, exist_ok=True)
    for name in os.listdir(out):
        path = os.path.join(out, name)
        if os.path.isfile(path):
            os.remove(path)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()  # one review, written and printed: fully deterministic
