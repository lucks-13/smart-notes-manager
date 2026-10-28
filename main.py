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
        self