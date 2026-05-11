from getkey import getkey, keys
from enum import StrEnum
import shutil
import sys
import os

from style_constants import COLORS, LOGOS
import text_generators as t_gen

# user for get char
if os.name == 'nt': import msvcrt
else:
    import tty
    import termios

class MODES(StrEnum):
    EDIT = 'e'
    VIEW = 'v'

class ACTIONS(StrEnum):
    TOGGLE_VIEW    = "1"
    CHANGE_LOGO_UP = keys.UP
    CHANGE_LOGO_DN = keys.DOWN
    CHANGE_COLOR_L = keys.LEFT
    CHANGE_COLOR_R = keys.RIGHT
    BACKSPACE      = keys.BACKSPACE


class AskeeCLI:

    def __init__(self):
        self.terminal_width = shutil.get_terminal_size().columns - 3
        self.terminal_height = shutil.get_terminal_size().lines - 3

        # Interaction variables
        self.mode = MODES.EDIT
        self.command = None
        self.user_input = []
        self.current_screen = "START_MENU" # TODO: Create constant later

        # Style variables
        self.current_color = COLORS.GREEN
        self.current_logo = LOGOS.ASKEE_LOGO_TOILET

        self.text_generator = t_gen.TextGenerator(self.terminal_width, self.terminal_height, self.current_color, self.current_logo)

        self.init_display()
        self.display()

    def init_display(self):
        self._clear_display()
        self.display(self.text_generator.start_screen())

    def _clear_display(self):
        os.system('clear' if os.name == 'posix' else 'cls')

    def handle_input(self):
        while self.mode == MODES.EDIT:
            current_char = getkey()
            if current_char in [action.value for action in ACTIONS]:
                print(current_char)
                self.exec_command(current_char)
            else:
                self.user_input.append(current_char)
                self.display_user_input()

    def display(self, string):
        print(string)

        if self.mode == MODES.EDIT:
            self.display_user_input()
            self.handle_input()
        else:
            print()

    def display_user_input(self):
        print("> " + "".join(self.user_input), end="\r\r")

    def exec_command(self, command):
        match command:
            case ACTIONS.CHANGE_COLOR_L:
                self.current_color = self.current_color.next()
                self.text_generator.current_color = self.current_color # TODO: remover a necessidade de trocar 2x o valor
            case ACTIONS.CHANGE_COLOR_R:
                self.current_color = self.current_color.previous()
                self.text_generator.current_color = self.current_color
            case ACTIONS.CHANGE_LOGO_UP:
                self.current_logo = self.current_logo.next()
                self.text_generator.current_logo = self.current_logo
            case ACTIONS.CHANGE_LOGO_DN:
                self.current_logo = self.current_logo.previous()
                self.text_generator.current_logo = self.current_logo
            case ACTIONS.BACKSPACE:
                self.user_input.pop()
            case _:
                pass

        self.init_display() # TODO: Remover a necessidade de ter que
                            # reiniciar a tela toda vez so p troca estilo



if __name__ == "__main__":
    try:
        app = AskeeCLI()
    except KeyboardInterrupt:
        sys.exit(0)