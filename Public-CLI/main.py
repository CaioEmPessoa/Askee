from getkey import getkey
from time import sleep
import termios
import shutil
import sys
import tty
import os

from Interatcion.cli_configs import CliConfigs
from Interatcion.actions_controll import MODES, Actions, Commands
from Interatcion.style_constants import COLORS, LOGOS
from PublicService import PublicService
import text_generators as t_gen

class AskeeCLI:
    def __init__(self, configs):
        self.configs = configs

        # Interaction variables
        self.user_input = self.configs.user_input

        self.text_generator = t_gen.TextGenerator(self.configs)
        self.public_service = PublicService(self, self.configs, self.text_generator)
        self.commands = Commands(self.public_service)
        self.actions = Actions(self.public_service)

        self.configs.current_screen = self.text_generator.start_screen()
        self.clear_display()
        self.reload_display("instant")

    def reload_display(self, display_mode="one-liner"):
        self.clear_display()
        self._display(
            self.configs.current_screen,
            display_mode
            )

    def clear_display(self):
        os.system('clear' if os.name == 'posix' else 'cls')

    def handle_input(self):
        # TODO: Create variable to controll and do not let
        # more than one instanec of this function run at the same time
        while self.configs.mode == MODES.EDIT:

            current_char = getkey()
            if current_char in [action.key for action in self.actions]:
                self.exec_action(current_char)
                continue

            elif current_char == "\n" and "".join(self.user_input) in [command.name for command in self.commands]:
                self.exec_command("".join(self.user_input))
                break

            # do not let user chars surpass terminal width
            if len(self.user_input) >= self.configs.terminal_width: continue
            if current_char == "\n":
                print("command not found! Type 'help' to see the list of the available commands.", end="\r")
                continue

            self.user_input.append(current_char)
            self.display_user_input()

    def _display(self, string, display_mode="instant"):
        print(self.configs.current_color)

        if not self.configs.animations:
            display_mode = "instant"

        if self.configs.current_user:
            print(
                f"Logged in as: {self.configs.current_user.get('username')}\n"
            )

        match display_mode:
            case "one-liner":
                for line in string.split("\n"):
                    print(line)
                    sleep(0.1)
            case "left-right-char":
                for char in string:
                    print(char, end='', flush=True)
                    sleep(0.01)
            case _:
                print(string)

        if self.configs.mode == MODES.EDIT:
            self.display_user_input()
            self.handle_input()

    def display_user_input(self):
        user_typed_string = "".join(self.user_input)

        print("  " * round(self.configs.terminal_width/2), end="\r\r")
        print("> " + user_typed_string, end="\r")

    def exec_action(self, action):
        self.actions.run(action)

    def exec_command(self, command):
        self.commands.run(command)

if __name__ == "__main__":
    try:
        app = AskeeCLI(CliConfigs())
    except KeyboardInterrupt:
        sys.exit(0)