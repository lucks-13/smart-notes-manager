import json
from pathlib import Path
from note import Note

app_data_dir = Path.home() / "smart-notes-manager"
default_storage_file = app_data_dir / "session.json"

def save_notes(notes, filename=None):
    storage_path = Path(filename) if filename else default_storage_file
    storage_path.parent.mkdir(parents=True, exist_ok=True)
    notes_data = [note.to_dict() for note in notes]
    with storage_path.open("w", encoding="utf-8") as file:
        json.dump(notes_data, file, indent=4)
    
    print(f"Saved {len(notes)} notes to {storage_path}")

def load_notes(filename=None):
    storage_path = Path(filename) if filename else default_storage_file
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