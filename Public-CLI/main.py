from getkey import getkey
from time import sleep
import termios
import shutil
import sys
import tty
import os

from cli_configs import CliConfigs
from constants.style_constants import COLORS, LOGOS
from constants.controll_constants import MODES, ACTIONS, Commands
from PublicService import PublicService
import text_generators as t_gen

#TODO WILL PROBABLY MOVE THIS IMPORT ELSEWHERE LATER
from AskeeRequests.Post import PostRequests

postRequests = PostRequests()

class AskeeCLI:
    def __init__(self, configs):
        self.configs = configs

        # Interaction variables
        self.mode = self.configs.mode
        self.user_input = self.configs.user_input

        self.public_service = PublicService(self, self.configs)
        self.text_generator = t_gen.TextGenerator(self.configs)
        self.commands = Commands(self.public_service)

        self.configs.current_screen = "START_MENU"
        self._clear_display()
        self.display(self.text_generator.start_screen(), "left-right-char")

    def reload_display(self, display_logo=""):
        self._clear_display()
        self.display(self.text_generator.start_screen(), display_logo)

    def _clear_display(self):
        os.system('clear' if os.name == 'posix' else 'cls')

    def handle_input(self):
        while self.mode == MODES.EDIT:
            current_char = getkey()
            if current_char in [action.value for action in ACTIONS]:
                self.exec_command(current_char) #TODO: need to send action dict value
            
            self.user_input.append(current_char)

            #TODO Need to better this check on god but i need to sleep xd lol kk
            if "".join(self.user_input) in [command.value for command in COMMANDS]:
                self.commands.execute()
                self.user_input.append(current_char) #TODO: need to send action dict value
                self.exec_command("".join(self.user_input))
            self.display_user_input()

    def display(self, string, display_mode="instant"):
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

        if self.mode == MODES.EDIT:
            self.display_user_input()
            self.handle_input()
        else:
            print("(view_mode)", end="\r\r")

    def display_user_input(self):
        print("> " + "".join(self.user_input), end="\r\r")

    def exec_command(self, command):
        command.get("action")()

if __name__ == "__main__":
    try:
        app = AskeeCLI(CliConfigs())
    except KeyboardInterrupt:
        sys.exit(0)