from shutil import get_terminal_size

from .style_constants import COLORS, LOGOS
from .actions_controll import MODES

class Configs:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_initialized'):
            return
        self._initialized = True

        # Terminal variables
        self.terminal_width = get_terminal_size().columns - 3
        self.terminal_height = get_terminal_size().lines - 3

        # Interaction variables
        self.mode = MODES.EDIT
        self.animations = True
        self.command = None
        self.user_input = []
        self.current_user = {}

        self.current_categories = []
        self.current_posts = []

        # Style variables
        self.current_color = COLORS.GREEN
        self.current_logo = LOGOS.ASKEE_LOGO_TOILET