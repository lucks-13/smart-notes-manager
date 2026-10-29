from datetime import datetime

class Note:
    counter = 1

    def __init__(self, title, content):
        self.id = Note.counter
        Note.counter += 1

        self.title = title
        self.content = content
        self.tags = set()

        self.created = datetime.now()
        self.updated = self.created

    def update_title(self, new_title):
        self.title = new_title
        self.updated = datetime.now()

    def update_content(self, new_content):
        self.content = new_content
        self.updated = datetime.now()

    def add_tag(self, tag):
        self.tags.add(tag)
        self.updated = datetime.now()

    def remove_tag(self, tag):
        if tag in self.tags:
            self.tags.remove(tag)
            self.updated = datetime.now()
        else:
            print(f"Tag \"{tag}\" does not exist.")

    def to_dict(self):
        return {
            "id" : self.id,
            "title" : self.title,
            "content" : self.content,
            "tags" : list(self.tags),
            "created" : self.created.isoformat(),
            "updated" : self.updated.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        note = cls(data["title"], data["content"])

        note.id = data["id"]
        note.tags = set(data["tags"])
        note.created = datetime.fromisoformat(data["created"])
        note.updated = datetime.fromisoformat(data["updated"])
        cls.counter = max(cls.counter, note.id + 1)

        return note

def find_note_by_id(notes, note_id):
    for note in notes:
        if note.id == note_id:
            return note
    return None