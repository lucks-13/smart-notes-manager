import unittest
from note import Note

class TestNote(unittest.TestCase):
    def test_create_note(self):
        note = Note("Title 1","Content 1")
        self.assertEqual(note.title,"Title 1")
        self.assertEqual(note.content,"Content 1")

    def test_update_title(self):
        note = Note("Title 1","Content 1")
        og_update = note.updated
        note.update_title("New_Title 1")
        self.assertEqual(note.title,"New_Title 1")
        self.assertGreaterEqual(note.updated, og_update)
    
    def test_update_content(self):
        note = Note("Title 1","Content 1")
        note.update_content("New_Content 1")
        self.assertEqual(note.content,"New_Content 1")

    def test_add_tag(self):
        note = Note("Title 1","Content 1")
        note.add_tag("Tag 1")
        self.assertIn("Tag 1", note.tags)

    def test_add_duplicate_tag(self):
        note = Note("Title 1","Content 1")
        note.add_tag("Tag 1")
        self.assertEqual(len(note.tags),1)

    def test_remove_tag(self):
        note = Note("Title 1","Content 1")
        note.add_tag("Tag 1")
        note.remove_tag("Tag 1")
        self.assertNotIn("Tag 1",note.tags)

    def test_remove_non_


if __name__ == "__main__":
    unittest.main()