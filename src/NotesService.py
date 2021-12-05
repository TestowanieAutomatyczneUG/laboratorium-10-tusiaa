from src.NotesStorage import *

class NotesService:

    def __init__(self):
        self.notes = NotesStorage()

    def add(self, note):
        self.notes.add(note)

    def clear(self):
        self.notes.clear()

    def averageOf(self, name):
        notes = self.notes.getAllNotesOf(name)
        value = 0
        for note in notes:
            value += note.get_note()
        if len(notes) == 0:
            return 0
        return value / len(notes)
        