import json
import os
import tempfile
import unittest

from note import Note
from storage import save_notes, load_notes

class TestStorage(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.filename = os.path.join(self.temp_dir.name, "test_session.json")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_save_notes(self):
        note = Note("Title 1", "Content 1")
        note.add_tag("Tag 1")
        save_notes([note], self.filename)
        self.assertTrue(os.path.exists(self.filename))
        with open(self.filename, "r") as file:
            data = json.load(file)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["title"], "Title 1")
        self.assertIn("Tag 1", data[0]["tags"])

    def test_load_notes(self):
        note = Note("Title 1", "Content 1")
        note.add_tag("Tag 1")
        save_notes([note], self.filename)
        loaded_notes = load_notes(self.filename)
        self.assertEqual(len(loaded_notes), 1)
        self.assertEqual(loaded_notes[0].title, "Title 1")
        self.assertEqual(loaded_notes[0].content, "Content 1")
        self.assertEqual(loaded_notes[0].tags, {"Tag 1"})
        self.assertEqual(loaded_notes[0].id, note.id)
        self.assertEqual(loaded_notes[0].created, note.created)
        self.assertEqual(loaded_notes[0].updated, note.updated)

    def test_load_missing_file(self):
        missing_filename = os.path.join(self.temp_dir.name, "missing.json")
        loaded_notes = load_notes(missing_filename)
        self.assertEqual(loaded_notes, [])

if __name__ == "__main__":
    unittest.main()