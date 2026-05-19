from getkey import keys
from enum import StrEnum

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
