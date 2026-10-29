import unittest
from note import Note

class TestNoteSerialization(unittest.TestCase):
    def test_to_dict(self):
        note = Note("Title 1", "Content 1")
        note.add_tag("Tag 1")
        data = note.to_dict()
        self.assertEqual(data["title"], "Title 1")
        self.assertEqual(data["content"], "Content 1")
        self.assertIn("Tag 1", data["tags"])
        self.assertEqual(data["id"], note.id)

    def test_from_dict(self):
        og = Note("Title 1", "Content 1")
        og.add_tag("Tag 1")
        data = og.to_dict()
        restore = Note.from_dict(data)
        self.assertEqual(restore.id, og.id)
        self.assertEqual(restore.title, og.title)
        self.assertEqual(restore.content, og.content)
        self.assertEqual(restore.tags, og.tags)
        self.assertEqual(restore.created, og.created)
        self.assertEqual(restore.updated, og.updated)

if __name__ == "__main__":
    unittest.main()