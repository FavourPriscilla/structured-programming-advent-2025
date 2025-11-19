from collections import Counter
import re

def parse_entry(line: str):
    """Parse entries like '2 apples' or 'apple' -> (quantity:int, name:str)."""
    line = line.strip()
    if not line:
        return 0, ""
    m = re.match(r'^\s*(\d+)\s*[xX]?\s+(.+)$', line)  # allow "2 x apples" or "2 apples"
    if m:
        return int(m.group(1)), m.group(2).strip().lower()
    # if no leading number, assume quantity 1
    return 1, line.lower()

def main():
    print("Enter shopping items, one per line.")
    print("Prefix with quantity if needed, e.g. '2 apples' or '3 x bananas'.")
    print("Press Enter on an empty line to finish.\n")

    counts = Counter()
    while True:
        try:
            s = input("> ")
        except EOFError:
            break
        if not s.strip():
            break
        qty, name = parse_entry(s)
        if qty > 0 and name:
            counts[name] += qty
        else:
            print("Ignored empty entry.")

    if not counts:
        print("\nNo items entered.")
        return

    print("\nAggregated shopping list:")
    for item, qty in counts.most_common():
        print(f"- {qty} x {item}")

if __name__ == "__main__":
    main()