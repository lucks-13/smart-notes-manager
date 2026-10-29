import json
import os
import tempfile
import unittest

from note import Note
from storage import save_notes, load_notes

class TestStorage(unittest,TestCase):
    def setUp(self):
        self.filename = os.path.join()