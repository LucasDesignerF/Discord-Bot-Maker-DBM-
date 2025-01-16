class EventHandler:
    def __init__(self):
        self.events = {}

    def add_event(self, name, function):
        self.events[name] = function

    def trigger_event(self, name, *args):
        if name in self.events:
            return self.events[name](*args)
        return None