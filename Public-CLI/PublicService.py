from pwinput import pwinput

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
        self.authRequests = Auth()
        self.commentRequests = Comment()
        self.categoryRequests = Category()

    # ============ ACTIONS FUNCTIONS ============
    def toggle_animations(self):
        self.configClass.animations = not self.configClass.animations
        print(f"Animations {"enabled" if self.configClass.animations else "disabled"}!", end="\r")

    def toggle_app_view(self):
        return
        # modes will not function as I first intended. TODO: change this function, probably remove it.
        current_mode = self.configClass.mode
        self.configClass.mode = MODES.VIEW if current_mode == MODES.EDIT else MODES.EDIT #TODO: import constants

    def change_app_logo(self, direction='right'): # direction = 'left' or 'right'
        display_mode = "one-liner"
        current_logo = self.configClass.current_logo
        self.configClass.current_logo = current_logo.previous() if direction=='left' else current_logo.next()

        self.configClass.current_screen.add_set(self.textGenerator.start_screen())
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

    def undo_screen(self):
        self.configClass.current_screen.undo()
        self.mainClass.reload_display()

    # ============ COMMAND VIEW FUNCTIONS ============
    def display_error(self, error_msg):
        error_logo = ERRORS.DEFAULT #TODO: change this to a random later
        self.configClass.current_screen.add_set(self.textGenerator.error_screen(
            error_logo, error_msg
            ))

        self.mainClass.reload_display("left-right-char")

    def view_home(self):
        home_string = self.textGenerator.start_screen()
        self.configClass.current_screen.add_set(home_string)

        self.mainClass.reload_display("left-right-char")

    def view_help(self):
        help_string = self.textGenerator.help_screen()
        self.configClass.current_screen.add_set(help_string)

        self.mainClass.reload_display("left-right-char")

    def view_posts(self):
        getAllPosts = self.postRequests.get_all().get("data")

        for i in range(1, len(getAllPosts)+1):
            getAllPosts[i-1].update({"tmp_id": i})

        self.configClass.current_posts = getAllPosts

        posts_string = self.textGenerator.posts(getAllPosts)
        self.configClass.current_screen.add_set(posts_string)

        self.mainClass.reload_display()

    # Not used in a single command. Stayied cause might be usefull, but was substituted by view category.
    def view_posts_by_category(self, categoryId=None):
        if not categoryId:
            if not self.configClass.current_categories:
                self.view_categories()
            self.start_type(clean=False)

            print("Please select the category number:")
            tmp_id = int(input("> "))-1

            self.end_type()

            categoryId = self.configClass.current_categories[tmp_id].get('id')

        getPosts = self.postRequests.get_posts_by_category_id(categoryId).jsonResponse.get("data")

        for i in range(1, len(getPosts)+1):
            getPosts[i-1].update({"tmp_id": i})

        self.configClass.current_posts = getPosts

        posts_string = self.textGenerator.posts(getPosts)
        self.configClass.current_screen.add_set(posts_string)

        self.mainClass.reload_display()

    def view_post(self, id=None):
        if not id:
            if not self.configClass.current_posts or not isinstance(self.configClass.current_posts, list):
                self.view_posts()
            self.start_type(clean=False)

            print("Please select the post number:")
            tmp_id = int(input("> "))-1

            self.end_type()

            id = self.configClass.current_posts[tmp_id].get('id')

        # Get post
        postResponse = self.postRequests.get_by_id(id)
        if postResponse.httpCode != 200: self.display_error(postResponse.jsonResponse.get('message'))

        postData = postResponse.jsonResponse.get('data')

        # Get post comments
        commentsResponse = self.commentRequests.get_comments_by_post_id(postData.get("id"))
        if commentsResponse.httpCode != 200: self.display_error(commentsResponse.jsonResponse.get('message'))
        postData["comments"] = self.append_comment_user(
            commentsResponse.jsonResponse.get('data')
        )

        # Get post user
        usersResponse = self.userRequests.get_by_id(postData.get("user_id"))
        postData["user"] = usersResponse.jsonResponse.get('data')

        posts_string = self.textGenerator.post(postData)
        self.configClass.current_screen.add_set(posts_string)
        self.configClass.current_posts = postData

        self.mainClass.reload_display()

    def view_categories(self):
        getAllCategories = self.categoryRequests.get_all().get("data")

        for i in range(1, len(getAllCategories)+1):
            getAllCategories[i-1].update({"tmp_id": i})

        self.configClass.current_categories = getAllCategories
        categories_string = self.textGenerator.categories(getAllCategories)
        self.configClass.current_screen.add_set(categories_string)

        self.mainClass.reload_display()

    def view_category(self, id=None):

        if not id:
            if not self.configClass.current_categories or not isinstance(self.configClass.current_categories, list):
                self.view_categories()
            self.start_type(clean=False)

            print("Please select the category number:")
            tmp_id = int(input("> "))-1

            self.end_type()

            id = self.configClass.current_categories[tmp_id].get('id')

        # Get category
        categoryResponse = self.categoryRequests.get_by_id(id)
        if categoryResponse.httpCode != 200: self.display_error(response.jsonResponse.get('message'))

        categoryData = categoryResponse.jsonResponse.get('data')

        # Get posts
        postsData = self.postRequests.get_posts_by_category_id(categoryData.get('id')).jsonResponse.get("data")

        for i in range(1, len(postsData)+1):
            postsData[i-1].update({"tmp_id": i})

        self.configClass.current_categories = categoryData
        self.configClass.current_posts = postsData

        category_string = self.textGenerator.category(categoryData, postsData)
        self.configClass.current_screen.add_set(category_string)

        self.mainClass.reload_display()

    def append_comment_user(self, comments):
        for comment in comments: # get user info
            usersResponse = self.userRequests.get_by_id(comment.get("user_id"))
            if usersResponse:
                comment.update({
                    'user': usersResponse.jsonResponse.get('data')
                    })

        return comments


    def view_post_comments(self, postId):
        commentsResponse = self.commentRequests.get_comments_by_post_id(postData.get("id"))
        if commentsResponse.httpCode != 200: self.display_error(response.jsonResponse.get('message'))

        commentsData = commentsResponse.jsonResponse.get('data')

        comments_string = self.textGenerator.comments(getAllComments)
        self.configClass.current_screen.append(comments_string) # += bc its used only at posts view. (or its supposed to)

        self.mainClass.reload_display()

    # ============ COMMAND INSERT FUNCTIONS ============

    def log_off(self):
        self.configClass.current_user = []
        self.view_home()

    def log_in(self):

        self.start_type(remaining_space=100)

        print("Welcome back to askee! \n")
        print("Please fill as the following to login back to your user: \n")

        user_mail = input("\n Email: \n> ")
        user_password = pwinput("\n Password: \n> ", mask="*")

        self.end_type()

        post_payload = {
            "email": user_mail,
            "password": user_password
        }
        login_response = self.authRequests.login(post_payload)

        if login_response.httpCode != 200: self.display_error(login_response.jsonResponse.get('message'))

        self.configClass.current_user = login_response.jsonResponse.get('data')

        self.view_home()


    def sign_up(self):

        self.start_type(remaining_space=100)

        print("Welcome to askee! \n")
        print("Please fill as the following to create your new user: \n")

        user_mail = input("\n Email: \n> ")
        user_password = getpass("\n Password: \n> ", mask="*")
        user_name = input("\n Username: \n> ")
        user_icon = input("\n Icon: \n> ")
        user_about = input("\n About: \n> ")

        self.end_type()

        post_payload = {
            "email":user_mail,
            "password":user_password,
            "name":user_name,
            "username":user_name,
            "icon":user_icon,
            "about":user_about,
            "is_moderator":False,
            "is_super":False
        }

        signing_response = self.authRequests.signup(post_payload)

        if signing_response.httpCode != 200: self.display_error(signing_response.jsonResponse.get('message'))

        input("You Signed-In sucessfully! On pressing 'enter' now you will be prompted to log-in with your newly created user.")

        self.log_in()

    def start_type(self, clean=True, remaining_space=4):
        self.configClass.mode = MODES.VIEW

        if clean:
            self.configClass.current_screen.add_set(self.textGenerator.fill_remaining_space("", remaining_space)) #TODO: change this view
            self.mainClass.reload_display("instant")

    def end_type(self):
        self.configClass.mode = MODES.EDIT

    def new_post(self):

        if not self.configClass.current_user or not self.configClass.current_user.get('is_moderator'):
            self.display_error("You are not logged-in or does not have the privileges to post something.")

        self.start_type()

        categories = self.categoryRequests.get_all()
        if not categories.get('data'): self.display_error(categories.get('message'))

        if self.configClass.current_categories and not isinstance(self.configClass.current_categories, list):
            category_id = self.configClass.current_categories.get('id')
            print(f"Posting at '{self.configClass.current_categories.get('name')}'...")
        else:
            print("Select the category of your post:")
            categories_list = []
            category_internal_id = 1
            for category in categories.get('data'):
                categories_list.append((category.get('id'), category_internal_id))
                print(category_internal_id, category.get('name'))

                category_internal_id += 1

            post_category = int(input("\n> "))
            category_id = categories_list[post_category-1][0]

        post_title = input("\n Post Title: \n> ")
        post_content = input("\n Post content: \n> ")

        self.end_type()

        post_payload = {
            "title": post_title,
            "content": post_content,
            "category_id": category_id,
            "user_id": self.configClass.current_user.get('id')
        }
        response = self.postRequests.post_new(post_payload)

        if response.httpCode != 200:
            self.display_error(response.jsonResponse.get('message'))
        else:
            self.view_post(response.jsonResponse.get('data').get('id'))

    def new_category(self):

        if not self.configClass.current_user or not self.configClass.current_user.get('is_super'):
            self.display_error("You are not logged-in or does not have the privileges to create a new category.")

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

    def new_comment(self):

        if not self.configClass.current_user:
            self.display_error("Please login before commenting.")

        if isinstance(self.configClass.current_posts, list):
            self.display_error("Please open a post to start commenting.")

        post_id = self.configClass.current_posts.get('id')

        self.start_type()

        comment_content = input("\n Content: \n> ")

        self.end_type()

        post_payload = {
            "user_id": self.configClass.current_user.get('id'),
            "post_id": post_id,
            "content": comment_content
        }
        response = self.commentRequests.post_new(post_payload)

        if response.httpCode != 200:
            self.display_error(response.jsonResponse.get('message'))
        else:
            self.view_post(post_id)

    def mod_user(self):
        # if not self.configClass.current_user or not self.configClass.current_user.get('is_super'):
        #     self.display_error("You are not logged-in or does not have the privileges to this command.")

        allUsers = self.userRequests.get_all().get('data')
        biggest_name = max([len(i.get('username')) for i in allUsers])
        user_counter = 0
        self.start_type()
        print("Please select the user to modify:\n")
        for user in allUsers:
            user_counter += 1
            print("  {} - {:<{}} : {} {} {}".format(
                user_counter,
                user.get('username'),
                biggest_name,
                "is a mod" if user.get('is_moderator') else "",
                "and" if user.get('is_super') and user.get('is_moderator') else "",
                "is a super" if user.get('is_super') else ""
            ))

        selected_user = int(input('\n> '))

        is_mod = input("Will this user be a mod? (y/N)\n> ")
        is_super = input("Will this user be a super? (y/N)\n> ")

        self.userRequests.update(
            allUsers[selected_user-1].get('id'),
            {
                "is_moderator": is_mod.upper() == "Y",
                "is_super": is_super.upper() == "Y"
            }
        )

        self.end_type()

        self.view_home()