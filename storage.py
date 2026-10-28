import json

def save_notes(notes):
    notes_data = [note.to_dict() for note in notes]
    with open("session.json","w") as file:
        json.dump(notes_data, file, indent=4)
    
    print(f"Saved {len(notes)} all notes to session.json")

def load_notes():
    with open("session.json","r") as file:
        notes = json.load(file)
    return notes