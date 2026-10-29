def find_note_by_id(notes, note_id):
    for note in notes:
        if note.id == note_id:
            return note
    return None