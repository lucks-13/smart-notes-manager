import unittest
from note import Note
from note_utils import find_note_by_id

class TestNoteUtils(unittest.TestCase):
    def setUp(self):
        self.note1 = Note("Title 1","Content 1")
        self.note1.add_tag