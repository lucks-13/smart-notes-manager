import unittest
from note import Note
from note_utils import find_note_by_id

class TestNoteUtils(unittest.TestCase):
    def setUp(self):
        self.note1 = Note("Title 1","Content 1")
        self.note1.add_tag("Tag 1")
        self.note2 = Note("Title 2","Content 2")
        self.note2.add_tag("Tag 2")
        self.notes = [self.note1, self.note2]

    def test_find_note_by_existing_id(self):
        result = find_note_by_id(self.notes, self.note1.id)
        self.assertIs(result, self.note1)
    
    def test_find_note_by_non_existent_id(self):
        result = find_note_by_id(self.notes, -1)
        self.assertIsNone(result)

    
