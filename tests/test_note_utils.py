import unittest
from note import Note
from note_utils import find_note_by_id, search_notes

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

    def test_search_by_content(self):
        results = search_notes(self.notes, 2, "Content")
        self.assertEqual(len(results),1)
        self.assertIs(results[0], self.note2)

    def test_search_by_tag(self):
        results = search_notes(self.notes, 3, "Tag 2")
        self.assertEqual(len(results),1)
        self.assertIs(results[0], self.note2)

    def test_search_is_case_insensitive(self):
        results = search_notes(self.notes, 1, "TITLE 1")
        self.assertEqual(len(results), 1)
        self.assertIs(results[0], self.note1)

    def test_search_with_no_matches(self):
        results = search_notes(self.notes, 1, "Title 3")
        self.assertEqual(results, [])

if __name__ == "__main__":
    unittest.main()

    
