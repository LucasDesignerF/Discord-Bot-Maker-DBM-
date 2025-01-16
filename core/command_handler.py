class CommandHandler:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def execute_command(self, name, *args):
        if name in self.commands:
            return self.commands[name](*args)
        return None