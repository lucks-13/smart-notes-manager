import unittest
from note import Note

class TestNoteSerialization(unittest.TestCase):
    def test_to_dict(self):
        self.note1 = Note("Title 1","Content 1")
        self.note1.add_tag("Tag 1")
        data = note.to_