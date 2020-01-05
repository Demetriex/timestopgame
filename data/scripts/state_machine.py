class StateMachine(object):
    def __init__(self):
        self.now = None
        self.state_name = None
        self.state_dict = {}
        self.state = None

    def setup(self, dictionary, start):
        self.state_dict = dictionary
        self.state = self.state_dict[start]

    def change_state(self):
        self.state_name, previous = self.state.next, self.state_name
        persist = self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup(persist)

    def draw(self, surface):
        self.state.draw(surface)

    def update(self, tick, keys, mkeys, mouse_pos):
        if self.state.done:
            self.change_state()
        self.state.update(tick, keys, mkeys, mouse_pos)


class State(object):
    def __init__(self):
        self.name = None
        self.persistent = None
        self.done = False

    def startup(self, persistent):
        self.persistent = persistent

    def cleanup(self):
        self.done = False
        return self.persistent

    def update(self, keys, mkeys, mouse_pos):
        pass
