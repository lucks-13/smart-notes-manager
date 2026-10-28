from note import Note
from storage import save_notes, load_notes

while True:
    print("====== Smart Notes Manager ======\n")
    print("1. Create a note")
    print("2. View all notes")
    print("3. Update a note")
    print("4. Delete a note")
    print("5. Search notes")
    print("6. Exit.")

    x = int(input("Choose an option :"))
    if not x or 1<=x<=6:
        continue
    break

if x==1:
    pass
elif x==2:
    pass
elif x==3:
    pass
elif x==4:
    pass
elif x==5:
    pass
elif x==6:
    pass

note1 = Note("title1","content1")
note2 = Note("title2","content2")

note1.update_title("new_title1")
note1.add_tag("1tag1")
note1.add_tag("2tag1")

notes = [note1, note2]

save_notes(notes)

loaded_notes = load_notes()

for note in loaded_notes:
    print(f"ID : {note.id}")
    print(f"title : {note.title}")
    print(f"content : {note.content}")
    print(f"Tags : {note.tags}")
    print("--------------")