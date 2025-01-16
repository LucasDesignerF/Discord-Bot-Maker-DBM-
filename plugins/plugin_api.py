class PluginAPI:
    def __init__(self):
        self.plugins = {}

    def register_plugin(self, name, plugin):
        self.plugins[name] = plugin

    def get_plugin(self, name):
        return self.plugins.get(name, None)