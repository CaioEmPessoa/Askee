from Interatcion.actions_controll import Commands, Actions

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

        actions_class = Actions('')
        commands_class = Commands('')

        string = "Actions:\n"
        string += "(Instant commands that work anywhere in the CLI by hotkeys)\n\n"

        biggest_desc = max([len(action.description) if action.hidden != True else 0 for action in actions_class])+2

        string += f"{'Action ':<{biggest_desc}}  | Key \n"
        string += f"{'-'*(biggest_desc+2)}|{'-'*10}\n"
        for action in actions_class:
            if action.hidden == True: continue
            string += f" {action.description:<{biggest_desc}} | {action.key_symbol}\n"

        string +=  "\n\nCommands :\n"
        string += "(Commands that needs to be written in the CLI)\n\n"

        biggest_desc = max([len(command.description) for command in commands_class])+2
        biggest_name = max([len(command.name) for command in commands_class])+2

        string += f"{"Command ":<{biggest_name}}   |  {"Description":<{biggest_desc}} \n"
        string += f"{'-'*(biggest_name+3)}|{'-'*(biggest_desc+1)}\n"
        for command in commands_class:
            string += f"  {command.name:<{biggest_name}} | {command.description:<{biggest_desc}}\n"

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
            string += "\n"
            string += f"{'-' * self.configs.terminal_width}\n\n"
            string += self.comments(post['comments'], fill=False)

        string += "\n"

        string += self.fill_remaining_space(string)

        return string

    def posts(self, posts, fill=True):
        string = "Posts :\n\n"

        if not posts: string += "  Nenhum post encontrado!"

        for post in posts:
            string += f"  {post["tmp_id"]} - {post["title"]}\n"
            string += f"{'-'*(len(post['title'])+10)}\n"
            string += f"  {post["content"]}\n"

            string += f"\n\n{'-' * self.configs.terminal_width}\n\n"

            string += "\n"

        if fill:
            string += self.fill_remaining_space(string)

        return string

    def comments(self, comments, fill=True):
        string = "Comments :\n\n"

        if not comments: string += "  Nenhum comentário encontrado!"

        for comment in comments:
            string += f"[!!!] - Name:\n"
            string += f"  {comment["content"]}\n\n"

            third_size = round(self.configs.terminal_width/3)
            string += f"{' ' * third_size}{'-' * third_size}{' ' * third_size}\n\n"
            string += "\n"

        if fill:
            string += self.fill_remaining_space(string)

        return string

    def category(self, category, posts):
        string = "Categoria :\n"

        string += f"   [{category['icon']}] - {category["name"]}\n"
        string += f"   Descrição : {category["description"]}\n"
        string += "\n"

        string += self.posts(posts, fill=False)

        string += self.fill_remaining_space(string)

        return string

    def categories(self, categories):
        string = "Categories :\n\n"

        if not categories: string += "  Nenhuma categoria encontrada!"

        for category in categories:
            string += f"{category['tmp_id']}  [{category['icon']}] - {category["name"]}\n"
            string += f"   Descrição : {category["description"]}\n"
            string += "\n"

        string += self.fill_remaining_space(string)

        return string