class EntityStateGroup:
    def __init__(self):
        self.states = {}
        self.current_state = None
        self.init = True

    def update(self):
        self.states[self.current_state].update()

    def add(self, name, action):
        new_state = EntityState(name, action)
        self.states[name] = new_state

class EntityState:
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def update(self):
        pass