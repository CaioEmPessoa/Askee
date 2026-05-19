from getkey import getkey
from time import sleep
import termios
import shutil
import sys
import tty
import os

from cli_configs import CliConfigs
from constants.style_constants import COLORS, LOGOS
from constants.controll_constants import MODES, ACTIONS, COMMANDS
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

        self.text_generator = t_gen.TextGenerator(self.configs)

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
                self.exec_command(current_char)
            #TODO Need to better this check on god but i need to sleep xd lol kk
            elif "".join(self.user_input)+current_char in [command.value for command in COMMANDS]:
                self.user_input.append(current_char)
                self.exec_command("".join(self.user_input))
            else:
                self.user_input.append(current_char)
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
                    sleep(0.00001)
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
        display_logo = ""
        # CHANGE THIS TO FUNCTIONS IN THE ENUM
        match command:
            case ACTIONS.CHANGE_COLOR_L:
                self.configs.current_color = self.configs.current_color.next()
                self.reload_display(display_logo)
            case ACTIONS.CHANGE_COLOR_R:
                self.configs.current_color = self.configs.current_color.previous()
                self.reload_display(display_logo)
            case ACTIONS.CHANGE_LOGO_UP:
                display_logo = "one-liner"
                self.configs.current_logo = self.configs.current_logo.next()
                self.reload_display(display_logo)
            case ACTIONS.CHANGE_LOGO_DN:
                display_logo = "one-liner"
                self.configs.current_logo = self.configs.current_logo.previous()
                self.reload_display(display_logo)

            case ACTIONS.TOGGLE_VIEW:
                self.configs.current_screen = "POSTS_VIEW"
                self.configs.mode = MODES.VIEW if self.configs.mode == MODES.EDIT else MODES.EDIT

            case ACTIONS.BACKSPACE:
                if len(self.user_input) > 0:
                    self.user_input.pop()
                    self.reload_display(display_logo)


            # WILL NEED TO CLEAN THIS UP IN A SEPARATED CLASS AND/OR FUNCTION LATER.
            case COMMANDS.LIST_POSTS:
                getAllPosts = postRequests.get_all().get("data")

                clean_post_str = ""

                for post in getAllPosts:
                    clean_post_str += f"Title: {post["title"]}\n"
                    clean_post_str += f"Content: {post["content"]}\n"
                    clean_post_str += "\n"

                self._clear_display()
                self.display(clean_post_str, "one-liner")
                self.user_input = [] # clean after sucessfull command run

            case _:
                self.display_user_input()
                pass



if __name__ == "__main__":
    try:
        app = AskeeCLI(CliConfigs())
    except KeyboardInterrupt:
        sys.exit(0)