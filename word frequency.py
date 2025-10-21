import re
from collections import Counter

def count_words(text):
    # normalize: lowercase, extract words
    words = re.findall(r"\b[a-zA-Z']+\b", text.lower())
    return Counter(words)

def main():
    print("Word Frequency Counter")
    mode = input("Enter 'p' to paste text or 'f' to read a file: ").strip().lower()
    if mode == 'f':
        path = input("Enter filename: ").strip()
        try:
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
        except Exception as e:
            print("Failed to read file:", e)
            return
    else:
        print("Paste your text. End input with a blank line (press Enter twice).")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        text = "\n".join(lines)

    counts = count_words(text)
    if not counts:
        print("No words found.")
        return

    print("\nMost common words:")
    for word, cnt in counts.most_common(20):
        print(f"{word}: {cnt}")

if __name__ == "__main__":
    main()