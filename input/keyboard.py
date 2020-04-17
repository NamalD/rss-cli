import click


class KeyEventHandler():
    def __init__(self):
        self.handlers = {}

    def handle_key(self, key, action):
        self.handlers[key] = action

    def handle_events(self):
        key = click.getchar()
        handler = self.handlers.get(key)

        if handler != None:
            handler()
