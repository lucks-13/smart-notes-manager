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
        if not notes:
            print("No notes found.")
        else:
            for note in notes:
                print(f"ID : {note.id}")
                print(f"Title : {note.title}")
                print(f"Content : {note.content}")
                print(f"Tags : {', '.join(note.tags) if note.tags else 'None'}")
                print(f"Created : {note.created}")
                print(f"Updated : {note.updated}")
                print("------------------------------------")
    elif x==3:
        if not notes:
            print("No notes available to update.")
            continue
        try:
            note_id = int(input("Enter ID of the note to update :"))
        except ValueError:
            print("Please enter te valid numeric ID.")
            continue
        selected_note = None
        for note in notes:
                if note.id == note_id:
                    selected_note = note
                    break
        if selected_note is None:
            print(f"No note found with ID ")
                    print("1. Update title")
                    print("2. Update content")
                    print("3. Add tag")
                    print("4. Remove tag\n")
                    try:
                        y = int(input("Choose what to update :"))
                    except ValueError:
                        print("Please enter te valid option.")
                        continue
                    if y == 1:
                        new_title = input("Enter new title :")
                        note.update_title(new_title)
                        save_notes(notes)
                        print("Note updated successfully.")
                    elif y == 2:
                        new_content = input("Enter new content :")
                        note.update_content(new_content)
                        save_notes(notes)
                        print("Note updated successfully.")
                    elif y == 3:
                        new_tag = input("Enter tag to add :")
                        note.add_tag(new_tag)
                        save_notes(notes)
                        print("Tag added successfully.")
                    elif y == 4:
                        r_tag = input("Enter tag to remove :")
                        note.remove_tag(r_tag)
                        save_notes(notes)
                        print("Tag removed successfully.")
                    else:
                        print("Invalid option.")
            else:
                print("Please enter te valid ID.")
                continue

    elif x==4:
        print("option 4")
    elif x==5:
        print("option 5")
    elif x==6:
        print("Good Bye.")
        break
    else:
        print("Invalid option.")