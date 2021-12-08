import unittest
from src.Note import *

class TestNote(unittest.TestCase):

    def test_note_init(self):
        self.tmp = Note("note", 5)
        self.assertNotEqual(self.tmp, None)

    def test_note_init_str_name(self):
        self.tmp = Note("note", 5)
        self.assertEqual(self.tmp.name, "note")

    def test_note_init_None_name(self):
        with self.assertRaises(Exception):
            Note(None, 5)

    def test_note_init_empty_name(self):
        with self.assertRaises(Exception):
            Note("", 5)

    def test_note_init_int_name(self):
        with self.assertRaises(TypeError):
            Note(5, 5)

    def test_note_init_float_name(self):
        with self.assertRaises(TypeError):
            Note(5.5, 5)

    def test_note_init_bool_name(self):
        with self.assertRaises(TypeError):
            Note(True, 5)

    def test_note_init_array_Name(self):
        with self.assertRaises(TypeError):
            Note([1, 2, 3], 5)

    def test_note_init_object_name(self):
        with self.assertRaises(TypeError):
            Note({1: 2, 3: 4}, 5)

    def test_note_init_None_note(self):
        with self.assertRaises(TypeError):
            Note("note", None)

    def test_note_init_empty_note(self):
        with self.assertRaises(TypeError):
            Note("note", "")

    def test_note_init_str_note(self):
        with self.assertRaises(TypeError):
            Note("note", "note")

    def test_note_init_bool_note(self):
        with self.assertRaises(TypeError):
            Note("note", True)

    def test_note_init_array_note(self):
        with self.assertRaises(TypeError):
            Note("note", [1, 2, 3])

    def test_note_init_object_note(self):
        with self.assertRaises(TypeError):
            Note("note", {1: 2, 3: 4})

    def test_note_init_int_note(self):
        self.tmp = Note("note", 5)
        self.assertEqual(self.tmp.note, 5.0)

    def test_note_init_float_note(self):
        self.tmp = Note("note", 5.5)
        self.assertEqual(self.tmp.note, 5.5)

    def test_note_init_note_to_small(self):
        with self.assertRaises(Exception):
            Note("note", 1)

    def test_note_init_note_to_big(self):
        with self.assertRaises(Exception):
            Note("note", 6.5)

    def test_note_get_name(self):
        self.tmp = Note("note", 5)
        self.assertEqual(self.tmp.get_name(), "note")

    def test_note_get_note(self):
        self.tmp = Note("note", 5)
        self.assertEqual(self.tmp.get_note(), 5.0)

    def test_note_set_name(self):
        self.tmp = Note("note", 5)
        self.tmp.set_name("note2")
        self.assertEqual(self.tmp.name, "note2")

    def test_note_set_name_None(self):
        self.tmp = Note("note", 5)
        with self.assertRaises(Exception):
            self.tmp.set_name(None)

    def test_note_set_name_empty(self):
        self.tmp = Note("note", 5)
        with self.assertRaises(Exception):
            self.tmp.set_name("")

    def test_note_set_name_int(self):
        self.tmp = Note("note", 5)
        with self.assertRaises(TypeError):
            self.tmp.set_name(5)

    def test_note_set_name_float(self):
        self.tmp = Note("note", 5)
        with self.assertRaises(TypeError):
            self.tmp.set_name(5.5)

    def test_note_set_name_bool(self):
        self.tmp = Note("note", 5)
        with self.assertRaises(TypeError):
            self.tmp.set_name(True)

    def test_note_set_name_array(self):
        self.tmp = Note("note", 5)
        with self.assertRaises(TypeError):
            self.tmp.set_name([1, 2, 3])

    def test_note_set_name_object(self):
        self.tmp = Note("note", 5)
        with self.assertRaises(TypeError):
            self.tmp.set_name({1: 2, 3: 4})

    def test_note_set_note_float(self):
        self.tmp = Note("note", 5)
        self.tmp.set_note(5.5)
        self.assertEqual(self.tmp.note, 5.5)

    def test_note_set_note_int(self):
        self.tmp = Note("note", 5.5)
        self.tmp.set_note(5)
        self.assertEqual(self.tmp.note, 5.0)

    def test_note_set_note_to_small(self):
        self.tmp = Note("note", 5)
        with self.assertRaises(Exception):
            self.tmp.set_note(1)

    def test_note_set_note_to_big(self):
        self.tmp = Note("note", 5)
        with self.assertRaises(Exception):
            self.tmp.set_note(6.5)

    def test_note_set_note_str(self):
        self.tmp = Note("note", 5)
        with self.assertRaises(TypeError):
            self.tmp.set_note("note")

    def test_note_set_note_bool(self):
        self.tmp = Note("note", 5)
        with self.assertRaises(TypeError):
            self.tmp.set_note(True)

    def test_note_set_note_array(self):
        self.tmp = Note("note", 5)
        with self.assertRaises(TypeError):
            self.tmp.set_note([1, 2, 3])

    def test_note_set_note_object(self):
        self.tmp = Note("note", 5)
        with self.assertRaises(TypeError):
            self.tmp.set_note({1: 2, 3: 4})

    def test_note_set_note_None(self):
        self.tmp = Note("note", 5)
        with self.assertRaises(TypeError):
            self.tmp.set_note(None)
        

