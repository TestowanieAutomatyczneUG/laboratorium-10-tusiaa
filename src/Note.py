class Note:
    def __init__(self, name: str, note: float):
        if name is None:
            raise Exception("Name cannot be None")
        if name == "":
            raise Exception("Name cannot be empty")
        if not isinstance(name, str):
            raise TypeError("Name must be str")    
        if (not isinstance(note, float) and not isinstance(note, int)) or isinstance(note, bool):
            raise TypeError("Note must be numeric")
        note = float(note)
        if note < 2 or note > 6:
            raise Exception("Note must be between 2 and 6")
        self.note = note
        self.name = name

    def get_note(self):
        return self.note

    def get_name(self):
        return self.name

    def set_note(self, note: float):
        if (not isinstance(note, float) and not isinstance(note, int)) or isinstance(note, bool):
            raise TypeError("Note must be numeric")
        note = float(note)
        if note < 2 or note > 6:
            raise Exception("Note must be between 2 and 6")
        self.note = note

    def set_name(self, name: str):
        if name is None:
            raise Exception("Name cannot be None")
        if name == "":
            raise Exception("Name cannot be empty")
        if not isinstance(name, str):
            raise TypeError("Name must be str")
        self.name = name