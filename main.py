import json
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

    def update_title()