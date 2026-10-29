import unittest
from note import Note

class TestNote(unittest.TestCase):
    def test_create_note(self):
        note = Note("Title 1","Content 1")
        self.assertEqual(note.title,"Title 1")
        self.assertEqual(note.content,"Content 1")

if __name__ == "__main__":
    unittest.main()