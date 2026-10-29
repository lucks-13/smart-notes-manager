import unittest
from note import Note

class TestNoteSerialization(unittest.TestCase):
    def test_to_dict(self):
        note = Note("Title 1", "Content 1")
        note.add_tag("Tag 1")
        data = note.to_dict()
        self.assertEqual(data["title"], "Title 1")
        self.assertEqual(data["content"], "Content 1")
        self.assertIn(data["tags"], "Tag 1")
        self.assertEqual(data["id"], note.id)

    def test_from_dict(self):
        og = Note("Title 1", "Content 1")
        