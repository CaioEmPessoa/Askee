class TextGenerator:
    def __init__(self, configs):
        self.terminal_width = configs.terminal_width
        self.terminal_height = configs.terminal_height

        self.current_color = configs.current_color
        self.current_logo = configs.current_logo

    def fill_remaining_space(self, string):
        remaining_space = self.terminal_height - string.count('\n')
        return "".join('\n' for i in range(remaining_space))

    def start_screen(self):
        string = self.generic(self.current_logo) # start string
        string += "\n"
        string += " Type 'help' for help.\n"
        string += '   ↑ ↓ Change the logo\n'
        string += '   ← → Change CLI colors\n'

        string += self.fill_remaining_space(string)
        return string

    def generic(self, string):
        return self.current_color + string