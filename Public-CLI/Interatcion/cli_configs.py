from shutil import get_terminal_size

from PublicService import PublicService

from .style_constants import COLORS, LOGOS
from .actions_controll import MODES

class CliConfigs():
    def __init__(self):
        # Terminal variables
        self.terminal_width = get_terminal_size().columns - 3
        self.terminal_height = get_terminal_size().lines - 3

        # Interaction variables
        self.mode = MODES.EDIT
        self.command = None
        self.user_input = []
        self.current_screen = "START_MENU"

        self.current_categories = []
        self.current_posts = []

        # Style variables
        self.current_color = COLORS.GREEN
        self.current_logo = LOGOS.ASKEE_LOGO_TOILET