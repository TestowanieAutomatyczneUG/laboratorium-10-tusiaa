import unittest
from unittest.mock import *
from src.Note import *
from src.NotesService import *

class TestNoteService(unittest.TestCase):

    def setUp(self):
        self.test_object = NotesService()

    @patch.object(NotesStorage, 'getAllNotesOf')
    def test_averageOf(self, mock_method):
        mock_method.return_value = [Note("note", 3), Note("note", 4), Note("note", 5)]
        result = self.test_object.averageOf("note")
        self.assertEqual(4, result, 'return value incorrect')

    @patch.object(NotesStorage, 'getAllNotesOf')
    def test_averageOf_0Notes(self, mock_method):
        mock_method.return_value = []
        result = self.test_object.averageOf("note")
        self.assertEqual(0, result, 'return value incorrect')

    @patch.object(NotesStorage, 'add')
    def test_add(self, mock_method):
        note = Note("note", 3)
        self.test_object.add(note)
        mock_method.assert_called_once_with(note)

    @patch.object(NotesStorage, 'clear')
    def test_clear(self, mock_method):
        self.test_object.clear()
        mock_method.assert_called_once_with()

    def tearDown(self):
        del self.test_object