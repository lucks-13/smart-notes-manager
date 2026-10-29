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

def search_notes(notes, search_option, word):
    word = word.strip().lower()
    results = []
    for note in notes:
        if search_option == 1 and word in note.title.lower():
            results.append(note)
                elif search_option == 2 and word in note.content.lower():
                    results.append(note)
                elif search_option == 3 and any(word in tag.lower() for tag in note.tags) :
                    results.append(note)