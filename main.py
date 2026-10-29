from note import Note
from note_utils import find_note_by_id, display_note
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
                
    elif x==3:
        if not notes:
            print("No notes available to update.")
            continue
        try:
            note_id = int(input("Enter ID of the note to update :"))
        except ValueError:
            print("Please enter a valid numeric ID.")
            continue
        selected_note = find_note_by_id(notes, note_id)
        if selected_note is None:
            print(f"No note found with ID {note_id}.")
            continue
        print(f"\nSelected note : {selected_note.title}")
        print("\n1. Update title")
        print("2. Update content")
        print("3. Add tag")
        print("4. Remove tag")
        print("5. Cancel")
        try:
            y = int(input("Choose what to update :"))
        except ValueError:
            print("Please enter te valid option.")
            continue
        if y == 1:
            new_title = input("Enter new title :").strip()
            if not new_title:
                print("Title cannot be empty.")
                continue
            selected_note.update_title(new_title)
            save_notes(notes)
            print("Note title updated successfully.")
        elif y == 2:
            new_content = input("Enter new content :").strip()
            selected_note.update_content(new_content)
            save_notes(notes)
            print("Note content updated successfully.")
        elif y == 3:
            new_tag = input("Enter tag to add :").strip()
            if not new_tag:
                print("Tag cannot be empty.")
                continue
            if new_tag in selected_note.tags:
                print(f"Tag \"{new_tag}\" already exists.")
            else:
                selected_note.add_tag(new_tag)
                save_notes(notes)
                print("Tag added successfully.")
        elif y == 4:
            if not selected_note.tags:
                print("This note no tags.")
                continue
            print("Existing tags : ",", ".join(sorted(selected_note.tags)))
            r_tag = input("Enter tag to remove : ").strip()
            if r_tag in selected_note.tags:
                selected_note.remove_tag(r_tag)
                save_notes(notes)
                print("Tag removed successfully.")
            else:
                print(f"Tag \"{r_tag}\" does not exist.")
        elif y == 5:
            print("Update cancelled.")
        else:
            print("Invalid option.")
    elif x==4:
        if not notes:
            print("No note available to delete.")
            continue
        try:
            note_id = int(input("Enter ID of the note to delete : "))
        except ValueError:
            print("Please enter a valid numeric ID.")
            continue
        selected_note = find_note_by_id(notes, note_id)
        if selected_note is None:
            print(f"No note found with ID {note_id}.")
            continue
        confirmation = input(f"Are you sure you want to delete \"{selected_note.title}\" ? (y/n) : ").strip().lower()
        if confirmation in ("y","yes"):
            notes.remove(selected_note)
            save_notes(notes)
            print("Note deleted successfully.")
        elif confirmation in ("n","no"):
            print("Operation cancelled.")
        else:
            print("Invalid confirmation. Operation cancelled.")

    elif x==5:
        if not notes:
            print("No notes available to search.")
            continue
        print("\n====== Search Notes ======")
        print("1. Search by title")
        print("2. Search by content")
        print("3. Search by tag")
        try:
            search_option = int(input("Choose a search type : "))
        except ValueError:
            print("Please enter a valid option.")
            continue
        if search_option not in (1,2,3):
            print("Invalid option.")
            continue
        word = input("Enter search word : ").strip().lower()
        if not word:
            print("Search word cannot be empty.")
            continue
        results = []
        for note in notes:
            if search_option == 1 and word in note.title.lower():
                results.append(note)
            elif search_option == 2 and word in note.content.lower():
                results.append(note)
            elif search_option == 3 and any(word in tag.lower() for tag in note.tags) :
                results.append(note)
        if results:
            print(f"\nFound {len(results)} matching notes : \n")
            for note in results:
                print(f"ID : {note.id}")
                print(f"Title : {note.title}")
                print(f"Content : {note.content}")
                print(f"Tags : {', '.join(sorted(note.tags)) if note.tags else 'None'}")
                print("-----------------------------------")
        else:
            print("No matching notes found.")
    elif x==6:
        print("Good Bye.")
        break
    else:
        print("Invalid option.")
