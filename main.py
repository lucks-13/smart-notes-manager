from note import Note
from storage import save_notes, load_notes

notes = load_notes()

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
        title = input("Enter note title :")
        content = input("Enter note content :")
        note = Note(title, content)
        notes.append(note)
        save_notes(notes)
        print(f"Note \"{title}\" created successfully! ID : {note.id}")
    elif x==2:
        print("====== Your Notes ======\n")
        for note in notes:
            print("ID : {note.id}")
            print("Content : {note.content}")
            print("Tags : {note.tags}")
            print("Created : {note.created}")
            print("Updated : {note.updated}")
            print("------------------------")
    elif x==3:
        print("option 3")
    elif x==4:
        print("option 4")
    elif x==5:
        print("option 5")
    elif x==6:
        print("Good Bye.")
        break
    else:
        print("Invalid option.")