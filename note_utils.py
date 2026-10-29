def find_note_by_id(notes, note_id):
    for note in notes:
        if note.id == note_id:
            return note
    return None

def display_note(note):
    print(f"ID : {note.id}")
    print(f"Title : {note.title}")
    print(f"Content : {note.content}")
    print(f"Tags : {', '.join(sorted(note.tags)) if note.tags else 'None'}")
    print(f"Created : {note.created}")
    print(f"Updated : {note.updated}")
    print("------------------------------------")