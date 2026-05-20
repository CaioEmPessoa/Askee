
from AskeeRequests import *

class PublicService:
    def __init__(self, main, config):
        self.mainClass = main
        self.configClass = config

        self.postRequests = Post()

    # ============ ACTIONS FUNCTIONS ============
    def toggle_app_view(self):
        current_mode = self.configClass.mode
        self.configClass.mode = MODES.VIEW if current_mode == MODES.EDIT else MODES.EDIT #TODO: import constants

    def change_app_logo(self, direction='right'): # direction = 'left' or 'right'
        display_logo = "one-liner"
        current_logo = self.configClass.current_logo
        self.configClass.current_logo = current_logo.previous() if direction=='left' else current_logo.next()
        self.mainClass.reload_display(display_logo)

    def change_app_color(self, direction='right'):
        display_logo = "instant"
        current_color = self.configClass.current_color
        self.configClass.current_color = current_color.previous() if direction=="left" else current_color.next
        self.mainClass.reload_display(display_logo)

    def backspace_action(self):
        if len(self.mainClass.user_input) > 0:
            self.mainClass.user_input.pop()
            self.mainClass.reload_display()

    # ============ COMMANDS FUNCTIONS ============
    def view_posts(self):
        getAllPosts = self.postRequests.get_all().get("data")

        clean_post_str = ""

        for post in getAllPosts:
            clean_post_str += f"Title: {post["title"]}\n"
            clean_post_str += f"Content: {post["content"]}\n"
            clean_post_str += "\n"

        self.mainClass._clear_display()
        self.mainClass.display(clean_post_str, "one-liner")
        self.mainClass.user_input = [] # clean after sucessfull command run
