import keyboard

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

if __name__ == "__main__":
    originator = Originator("State1")
    caretaker = Caretaker()

    caretaker.add_memento(originator.create_memento())

    originator.set_state("State2")
    caretaker.add_memento(originator.create_memento())

    originator.set_state("State3")
    caretaker.add_memento(originator.create_memento())

    def undo():
        if caretaker._mementos:
            memento = caretaker._mementos.pop()
            originator.restore_from_memento(memento)

    keyboard.add_hotkey('ctrl+z', undo)

    keyboard.wait()