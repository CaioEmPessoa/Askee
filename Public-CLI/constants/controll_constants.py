from getkey import keys
from enum import StrEnum

from ..PublicService import PublicService

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

class COMMANDS(StrEnum):
    HELP       = "help"
    LIST_POSTS = {
        "name": "view posts\n",              #TODO: remove \n hardcoded. Place it on validaton later.
        "action":PublicService().view_posts  #TODO: test this
    }
