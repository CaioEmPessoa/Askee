
from AskeeRequests import *

class PublicService:
    def __init__(self, main, config, textGenerator):
        self.mainClass = main
        self.configClass = config
        self.textGenerator = textGenerator

        self.postRequests = Post()
        self.userRequests = Users()
        self.commentRequests = Comment()
        self.categoryRequests = Category()

    # ============ ACTIONS FUNCTIONS ============
    def toggle_app_view(self):
        current_mode = self.configClass.mode
        self.configClass.mode = MODES.VIEW if current_mode == MODES.EDIT else MODES.EDIT #TODO: import constants

    def change_app_logo(self, direction='right'): # direction = 'left' or 'right'
        display_mode = "one-liner"
        current_logo = self.configClass.current_logo
        self.configClass.current_logo = current_logo.previous() if direction=='left' else current_logo.next()

        self.configClass.current_screen = self.textGenerator.start_screen()
        self.mainClass.reload_display(display_mode)

    def change_app_color(self, direction='right'):
        display_mode = "instant"
        current_color = self.configClass.current_color
        self.configClass.current_color = current_color.previous() if direction=="left" else current_color.next()
        self.mainClass.reload_display(display_mode)

    def backspace_action(self):
        if len(self.mainClass.user_input) > 0:
            self.mainClass.user_input.pop()
            self.mainClass.display_user_input()

    # ============ COMMANDS FUNCTIONS ============
    def view_home(self):
        home_string = self.textGenerator.start_screen()
        self.configClass.current_screen = home_string

        self.mainClass.reload_display("left-right-char")

    def view_help(self):
        help_string = self.textGenerator.help_screen()
        self.configClass.current_screen = help_string

        self.mainClass.reload_display("left-right-char")

    def view_posts(self):
        getAllPosts = self.postRequests.get_all().get("data")

        posts_string = self.textGenerator.posts(getAllPosts)
        self.configClass.current_screen = posts_string

        self.mainClass.reload_display()

    def view_comments(self):
        getAllComments = self.commentRequests.get_all().get("data")

        comments_string = self.textGenerator.comments(getAllComments)
        self.configClass.current_screen = comments_string

        self.mainClass.reload_display()

    def view_categories(self):
        getAllCategories = self.categoryRequests.get_all().get("data")

        categories_string = self.textGenerator.categories(getAllCategories)
        self.configClass.current_screen = categories_string

        self.mainClass.reload_display()