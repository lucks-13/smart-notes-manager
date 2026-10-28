import json
from note import Note

def save_notes(notes):
    notes_data = [note.to_dict() for note in notes]
    with open("session.json","w") as file:
        json.dump(notes_data, file, indent=4)
    
    print(f"Saved {len(notes)} all notes to session.json")

def load_notes():
    try:
        with open("session.json","r") as file:
            notes_data = json.load(file)
        notes = [Note.from_dict(data) for data in notes_data]
        return notes