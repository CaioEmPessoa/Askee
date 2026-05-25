from getkey import keys
from enum import StrEnum

class MODES(StrEnum):
    EDIT = 'e'
    VIEW = 'v'


class Action:
    def __init__(self, key, method="", description="", **kargs):
        self.key = key
        self.method = method
        self.description = description

        self.kargs = kargs

class Actions:
    '''Instant commands that work anywhere in the CLI by hotkeys'''
    TOGGLE_VIEW    = Action(keys.F1, "toggle_app_view")
    CHANGE_LOGO_UP = Action(keys.UP, "change_app_logo", direction='right')
    CHANGE_LOGO_DN = Action(keys.DOWN, "change_app_logo", direction='left')
    CHANGE_COLOR_L = Action(keys.LEFT, "change_app_color", direction='right')
    CHANGE_COLOR_R = Action(keys.RIGHT, "change_app_color", direction='left')
    BACKSPACE      = Action(keys.BACKSPACE, "backspace_action")

    def __init__(self, public_service=None):
        self.public_service = public_service

    @classmethod
    def __iter__(cls):
        for attr in vars(cls).values():
            if isinstance(attr, Action):
                yield attr

    def get(self, key):
        for action in self:
            if key == action.key:
                return action
        return None

    def execute(self, action):
        if self.public_service and action.method:
            method = getattr(self.public_service, action.method)
            return method(**action.kargs)
        return None

    def run(self, key):
        action = self.get(key)
        if action:
            return self.execute(action)
        return None

class Command:
    def __init__(self, name, method, description=""):
        self.name = name
        self.method = method
        self.description = description

class Commands:
    '''Commands that needs to be written in edit mode.'''
    HELP = Command("help", "view_help", "Shows the help message")
    HOME = Command("home", "view_home", "Shows the home")
    VIEW_POSTS = Command("view posts", "view_posts", "Shows all current posts")
    VIEW_COMMENTS = Command("view comments", "view_comments", "Shows all current comments")
    VIEW_CATEGORIES = Command("view categories", "view_categories", "Shows all current categories")

    NEW_POST = Command("new post", "new_post", "Add a new post")
    NEW_CATAEGORY = Command("new category", "new_category", "Add a new category")

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