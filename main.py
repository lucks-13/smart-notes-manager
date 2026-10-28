import json
from note import Note

note1 = Note("title1","content1")
note2 = Note("title2","content2")

note1.update_title("new_title1")
note1.add_tag("1tag1")
note1.add_tag("2tag1")

notes = [note1, note2]
notes_data = [note.to_dict() for note in notes]

with open("session.json","w") as file:
    json.dump(notes_data, file, indent=4)

print(f"Saved {len(notes)} all notes to session.json")