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

class Commands:
    HELP = ("help", "show_help")
    VIEW_POSTS = ("view posts", "view_posts")
    
    def __init__(self, public_service):
        self.publicService = public_service
    
    def execute(self, command, *args, **kwargs):
        _, method_name = command
        action = getattr(self.publicService, method_name)
        return action(*args, **kwargs)