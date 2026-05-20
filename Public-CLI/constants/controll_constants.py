from getkey import keys
from enum import StrEnum

class MODES(StrEnum):
    EDIT = 'e'
    VIEW = 'v'

class ACTIONS(StrEnum):
    TOGGLE_VIEW    = keys.F1
    CHANGE_LOGO_UP = keys.UP
    CHANGE_LOGO_DN = keys.DOWN
    CHANGE_COLOR_L = keys.LEFT
    CHANGE_COLOR_R = keys.RIGHT
    BACKSPACE      = keys.BACKSPACE

class Command:
    def __init__(self, name, method, description=""):
        self.name = name
        self.method = method
        self.description = description

class Commands:
    HELP = Command("help", "show_help", "Shows the help message")
    VIEW_POSTS = Command("view posts", "view_posts", "Shows all current posts")

    def __init__(self, public_service):
        self.publicService = public_service

    # makes this class an iterable
    @classmethod
    def __iter__(cls):
        for attr in vars(cls).values():
            if isinstance(attr, Command):
                yield attr

    def get(self, command_name):
        for cmd in self:
            if command_name == cmd.name:
                return cmd

    def execute(self, command, *args, **kwargs):
        action = getattr(self.publicService, command.method)
        return action(*args, **kwargs)

    def run(self, command_name, *args, **kwargs):
        return self.execute(self.get(command_name))