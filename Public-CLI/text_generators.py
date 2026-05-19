class TextGenerator:
    def __init__(self, configs):
        self.configs = configs

    def fill_remaining_space(self, string):
        remaining_space = self.configs.terminal_height - string.count('\n')
        return "".join('\n' for i in range(remaining_space))

    def start_screen(self):
        string = self.generic(self.configs.current_logo) # start string
        string += "\n"
        string += " Type 'help' for help.\n"
        string += '   ↑ ↓ Change the logo\n'
        string += '   ← → Change CLI colors\n'

        string += self.fill_remaining_space(string)
        return string

    def generic(self, string):
        return self.configs.current_color + string