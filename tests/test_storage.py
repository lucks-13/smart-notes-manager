import json
import os
import tempfile
import unittest

from note import Note
from storage import save_notes, load_notes

class TestStorage(unittest,TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.filename = os.path.join(self.temp_dir.name, "test_session.json")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_save_notes(self):
        note = Note("Title 1", "Content 1")
        note.add_tag()