import unittest
from unittest.mock import *
from parameterized import parameterized
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

    @parameterized.expand([
        ("", ValueError),
        (5, ValueError),
        (5.5, ValueError),
        (True, ValueError),
        (None, ValueError),
        ([1,2,3], ValueError),
        ({'name': 2, 'grades': 4}, ValueError),
    ])
    @patch.object(NotesStorage, 'getAllNotesOf')
    def test_averageOf_wrong_name(self, name, expected_exception, mock_method):
        mock_method.return_value = [Note("note", 3), Note("note", 4), Note("note", 5)]
        with self.assertRaises(expected_exception):
            self.test_object.averageOf(name)

    def tearDown(self):
        del self.test_object