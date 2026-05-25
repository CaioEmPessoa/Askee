class TextGenerator:
    def __init__(self, configs):
        self.configs = configs

    def fill_remaining_space(self, string, divide_ammount=1):
        remaining_space = round((self.configs.terminal_height / divide_ammount) - string.count('\n'))
        return "".join('\n' for i in range(remaining_space))

    def start_screen(self):
        string = self.configs.current_logo # start string
        string += "\n"
        string += " Type 'help' for help.\n"
        string += '   ↑ ↓ Change the logo\n'
        string += '   ← → Change CLI colors\n'

        string += self.fill_remaining_space(string)
        return string

    def help_screen(self):
        string =  "List of all commands/actions :\n\n"
        string += "view posts <category> : Show all posts. Can search by category\n"
        string += "view categories       : Show all categories\n"
        string += "view users <active>   : Show all users. Can search by active (bool)\n"

        string += self.fill_remaining_space(string)

        return string

    def error_screen(self, error_logo, error_msg):
        string =  error_logo
        string += f"\n\n '{error_msg}'"

        string += self.fill_remaining_space(string)

        return string

    def post(self, post):
        string = f" POST # {post["title"]}\n\n"

        string += f"  {post["content"]}\n"

        if post.get('comments'):
            string += self.comment(post['comments']) # test if works

        string += "\n"

        string += self.fill_remaining_space(string)

        return string

    def posts(self, posts):
        string = "Posts :\n\n"

        if not posts: string += "  Nenhum post encontrado!"

        for post in posts:
            string += f"Title: {post["title"]}\n"
            string += f"Content: {post["content"]}\n"

            if post.get('comments'):
                string += self.comment(post['comments']) # test if works

            string += "\n"

        string += self.fill_remaining_space(string)

        return string

    def comments(self, comments):
        string = "Comments :\n\n"

        if not comments: string += "  Nenhum comentário encontrado!"

        for comment in comments:
            string += f"Post (id): {comment["post_id"]}\n"
            string += f"User (id): {comment["user_id"]}\n"
            string += f"Content: {comment["content"]}\n"
            string += "\n"

        string += self.fill_remaining_space(string)

        return string

    def category(self, category):
        string = "Categoria :\n\n"

        string += f"   [{category['icon']}] - {category["name"]}\n"
        string += f"   Descrição : {category["description"]}\n"
        string += "\n"

        string += self.fill_remaining_space(string)

        return string

    def categories(self, categories):
        string = "Categories :\n\n"

        if not categories: string += "  Nenhuma categoria encontrada!"

        for category in categories:
            string += f"   [{category['icon']}] - {category["name"]}\n"
            string += f"   Descrição : {category["description"]}\n"
            string += "\n"

        string += self.fill_remaining_space(string)

        return string