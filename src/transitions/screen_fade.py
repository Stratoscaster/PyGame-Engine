import pygame
import tools.constants as c
from tools.entity_state import EntityStateGroup
import tools.color_list as colors


class ScreenFade:
    def __init__(self):
        self.image = pygame.Surface(c.NATIVE_SIZE)
        self.color = colors.BLACK
        self.image.fill(self.color)
        self.alpha = 0.0
        self.increment = 1.0
        self.decrement = 1.0
        self.min_alpha = 0.0
        self.max_alpha = 255.0
        self.image.set_alpha(self.max_alpha)
        self.states = EntityStateGroup()
        self.states.add('FADE_IN', self.state_fade_in)
        self.states.add('PAUSE', self.state_pause)
        self.states.add('FADE_OUT', self.state_fade_out)

    def update(self):
        pass

    def state_fade_in(self):
        pass

    def state_pause(self):
        pass

    def state_fade_out(self):
        pass

    def set_alpha(self, value):
        self.image.set_alpha(value)