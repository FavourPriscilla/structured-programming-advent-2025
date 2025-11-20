import json
import os
from collections import defaultdict, Counter
from datetime import datetime

DATA_FILE = "notes.json"

def load_notes():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_notes(notes):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)

def add_note(notes):
    title = input("Title: ").strip()
    body = input("Body: ").strip()
    tags = input("Tags (comma-separated): ").strip()
    tag_list = [t.strip().lower() for t in tags.split(",") if t.strip()]
    note = {
        "title": title,
        "body": body,
        "tags": tag_list,
        "created": datetime.now().isoformat()
    }
    notes.append(note)
    print("Note added.")

def list_notes(notes):
    if not notes:
        print("No notes.")
        return
    for i, n in enumerate(notes, 1):
        tags = ", ".join(n["tags"]) or "(no tags)"
        print(f"{i}. {n['title']}  [{tags}]  ({n['created'][:19]})")

def list_by_tag(notes):
    tag = input("Tag to filter by: ").strip().lower()
    found = [n for n in notes if tag in n["tags"]]
    if not found:
        print(f"No notes found with tag '{tag}'.")
        return
    for i, n in enumerate(found, 1):
        print(f"{i}. {n['title']} - {n['created'][:19]}")
        print(f"   {n['body']}")

def tag_summary(notes):
    counter = Counter()
    groups = defaultdict(list)
    for n in notes:
        for t in n["tags"]:
            counter[t] += 1
            groups[t].append(n["title"])
    if not counter:
        print("No tags yet.")
        return
    print("Tag counts:")
    for tag, cnt in counter.most_common():
        print(f"- {tag}: {cnt} (examples: {', '.join(groups[tag][:3])})")

def main():
    notes = load_notes()
    while True:
        print("\nNotes — Menu")
        print("1. Add note")
        print("2. List notes")
        print("3. List notes by tag")
        print("4. Tag summary")
        print("5. Save & exit")
        print("6. Exit without saving")
        choice = input("Choose (1-6): ").strip()
        if choice == "1":
            add_note(notes)
        elif choice == "2":
            list_notes(notes)
        elif choice == "3":
            list_by_tag(notes)
        elif choice == "4":
            tag_summary(notes)
        elif choice == "5":
            save_notes(notes)
            print(f"Saved to {DATA_FILE}. Goodbye.")
            break
        elif choice == "6":
            print("Goodbye (not saved).")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()