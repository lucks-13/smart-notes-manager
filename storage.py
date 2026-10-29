import json
from pathlib import Path
from note import Note

app_data_dir = Path.home() / "smart-notes-manager"
default_storage

def save_notes(notes, filename="session.json"):
    notes_data = [note.to_dict() for note in notes]
    with open(filename,"w") as file:
        json.dump(notes_data, file, indent=4)
    
    print(f"Saved {len(notes)} notes to {filename}")

def load_notes(filename="session.json"):
    try:
        with open(filename,"r") as file:
            notes_data = json.load(file)
        notes = [Note.from_dict(data) for data in notes_data]
        return notes
    except FileNotFoundError:
        print(f"{filename} file not found.")
        return []
    except json.JSONDecodeError:
        print(f"{filename} contains invalid Json.")
        return []