from getkey import keys
from enum import StrEnum

class MODES(StrEnum):
    EDIT = 'e'
    VIEW = 'v'


class Action:
    def __init__(self, key, method="", key_symbol="", description="", hidden=False, **kargs):
        self.key = key
        self.method = method
        self.key_symbol = key_symbol
        self.description = description
        self.hidden = hidden

        self.kargs = kargs

class Actions:
    '''Instant commands that work anywhere in the CLI by hotkeys'''
    TOGGLE_VIEW    = Action(keys.F1, "toggle_app_view", hidden=True)
    CHANGE_LOGO_UP = Action(keys.UP, "change_app_logo", '↑', "Changes the home logo", direction='right')
    CHANGE_LOGO_DN = Action(keys.DOWN, "change_app_logo", '↓', "Changes the home logo", direction='left')
    CHANGE_COLOR_L = Action(keys.LEFT, "change_app_color", '←', "Changes the CLI color", direction='right')
    CHANGE_COLOR_R = Action(keys.RIGHT, "change_app_color", '→', "Changes the CLI color", direction='left')
    TOGGLE_ANIMATION = Action(keys.TAB, "toggle_animations", '⭾', "Disable/Enables the CLI animations")
    BACKSPACE      = Action(keys.BACKSPACE, "backspace_action", hidden=True)

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

    SIGN_IN = Command("sign-in", "sign_up", "Sign-in into the askee network")
    LOGIN = Command("login", "log_in", "Log-in into the askee network")

    VIEW_POSTS = Command("view all posts", "view_posts", "Shows all current posts")
    VIEW_CATEGORIES = Command("view categories", "view_categories", "Shows all current categories")


    VIEW_CATEGORY = Command("view category", "view_category", "View a single category and its posts")
    VIEW_POST = Command("view post", "view_post", "View a single post")

    NEW_POST = Command("new post", "new_post", "Add a new post")
    NEW_CATAEGORY = Command("new category", "new_category", "Add a new category")
    NEW_COMMENT = Command("comment", "new_comment", "Add a new comment into a post")

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