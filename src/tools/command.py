class Command:

    def __init__(self, input_command):
        self.input_command = input_command

    def execute(self, actor):
        actor.user_input(self.input_command)