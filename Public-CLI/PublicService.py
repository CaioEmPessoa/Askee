
from AskeeRequests import *

from Interatcion.actions_controll import MODES
from Interatcion.style_constants import ERRORS

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
        return
        # modes will not function as I first intended. TODO: change this function, probably remove it.
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

    # ============ COMMAND VIEW FUNCTIONS ============
    def display_error(self, error_msg):
        error_logo = ERRORS.DEFAULT #TODO: change this to a random later
        self.configClass.current_screen = self.textGenerator.error_screen(
            error_logo, error_msg
            )

        self.mainClass.reload_display("left-right-char")

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

        for i in range(1, len(getAllPosts)+1):
            getAllPosts[i-1].update({"tmp_id": i})

        self.configClass.current_posts = getAllPosts

        posts_string = self.textGenerator.posts(getAllPosts)
        self.configClass.current_screen = posts_string

        self.mainClass.reload_display()

    def view_post(self, id=None):
        if not id:
            if not self.configClass.current_posts:
                self.view_posts()
            self.start_type(clean=False)

            print("Please select the post number:")
            tmp_id = int(input("> "))-1

            self.end_type()

            id = self.configClass.current_posts[tmp_id].get('id')

        postResponse = self.postRequests.get_by_id(id)
        if postResponse.httpCode != 200: self.display_error(response.jsonResponse.get('message'))

        postData = postResponse.jsonResponse.get('data')

        posts_string = self.textGenerator.post(postData)
        self.configClass.current_screen = posts_string

        self.mainClass.reload_display()

    def view_categories(self):
        getAllCategories = self.categoryRequests.get_all().get("data")

        for i in range(1, len(getAllCategories)+1):
            getAllCategories[i-1].update({"tmp_id": i})

        self.configClass.current_categories = getAllCategories
        categories_string = self.textGenerator.categories(getAllCategories)
        self.configClass.current_screen = categories_string

        self.mainClass.reload_display()

    def view_category(self, id=None):

        if not id:
            if not self.configClass.current_categories:
                self.view_categories()
            self.start_type(clean=False)

            print("Please select the category number:")
            tmp_id = int(input("> "))-1

            self.end_type()

            id = self.configClass.current_categories[tmp_id].get('id')

        postResponse = self.categoryRequests.get_by_id(id)
        if postResponse.httpCode != 200: self.display_error(response.jsonResponse.get('message'))

        categoryData = postResponse.jsonResponse.get('data')

        category_string = self.textGenerator.category(categoryData)
        self.configClass.current_screen = category_string

        self.mainClass.reload_display()

    def view_comments(self):
        getAllComments = self.commentRequests.get_all().get("data")

        comments_string = self.textGenerator.comments(getAllComments)
        self.configClass.current_screen = comments_string

        self.mainClass.reload_display()

    # ============ COMMAND INSERT FUNCTIONS ============

    def start_type(self, clean=True):
        self.configClass.mode = MODES.VIEW

        if clean:
            self.configClass.current_screen = self.textGenerator.fill_remaining_space("", 4) #TODO: change this view
            self.mainClass.reload_display("instant")

    def end_type(self):
        self.configClass.mode = MODES.EDIT

    def new_post(self):
        self.start_type()

        categories = self.categoryRequests.get_all()
        if not categories.get('data'): self.display_error(categories.get('message'))

        print("Select the category of your post:")
        categories_list = []
        category_internal_id = 1
        for category in categories.get('data'):
            categories_list.append((category.get('id'), category_internal_id))
            print(category_internal_id, category.get('name'))

            category_internal_id += 1

        post_category = int(input("\n> "))
        post_title = input("\n Post Title: \n> ")
        post_content = input("\n Post content: \n> ")

        self.end_type()

        post_payload = {
            "title": post_title,
            "content": post_content,
            "category_id": categories_list[post_category-1][0],
            "user_id": "mocado"
        }
        response = self.postRequests.post_new(post_payload)

        if response.httpCode != 200:
            self.display_error(response.jsonResponse.get('message'))
        else:
            self.view_post(response.jsonResponse.get('data').get('id'))

    def new_category(self):
        self.start_type()

        category_name = input("\n Category name: \n> ")
        category_description = input("\n Category description: \n> ")
        category_icon = input("\n Category icon: \n> ")

        self.end_type()

        post_payload = {
            "name": category_name,
            "description": category_description,
            "icon": category_icon
        }
        response = self.categoryRequests.post_new(post_payload)

        if response.httpCode != 200:
            self.display_error(response.jsonResponse.get('message'))
        else:
            self.view_category(response.jsonResponse.get('data').get('id'))