from note import Note
from storage import save_notes, load_notes

notes = load_notes

while True:
    print("====== Smart Notes Manager ======\n")
    print("1. Create a note")
    print("2. View all notes")
    print("3. Update a note")
    print("4. Delete a note")
    print("5. Search notes")
    print("6. Exit.")

    try:
        x = int(input("Choose an option :"))
    except ValueError:
        print("Please enter te valid number.")
        continue

    if x==1:
        print("")