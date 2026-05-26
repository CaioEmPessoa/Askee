# Design Pattern: Memento

class Originator:
    def __init__(self, state):
        self._state = state

    def create_memento(self):
        return Memento(self._state)

    def restore_from_memento(self, memento):
        self._state = memento.get_state()

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state

class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

class Caretaker:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        self._mementos.append(memento)

    def get_memento(self, index):
        return self._mementos[index]


class CurrentScreen:
    def __init__(self, initial_state):
        self.originator = Originator(initial_state)
        self.caretaker = Caretaker()

    def get(self):
        return self.originator.get_state()

    def add_set(self, string):
        self.originator.set_state(string)
        self.caretaker.add_memento(self.originator.create_memento())

    def append(self, state):
        screen_string  = self.originator.get_state()
        screen_string += state
        self.add_set(screen_string)

    def undo(self):
        if self.caretaker._mementos:
            memento_state = self.caretaker._mementos.pop()
            self.originator.restore_from_memento(memento_state)
