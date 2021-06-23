import pygame
from tools import constants as c
from tools.controller import Controller
from game_states.splash_screen import SplashScreen

# from splash_screen import SplashScreen

def get_display():
    display = pygame.display.set_mode(c.DISPLAY_SIZE)
    return display

def get_clock():
    clock = pygame.time.Clock()
    return clock

def get_game_states():
    game_states = {c.SPLASH_SCREEN : SplashScreen}
    return game_states

def get_controller(display, clock, game_states, starting_state):
    controller = Controller(display, clock, game_states, starting_state)
    return controller

def load_gfx():
    print('gfx not config')
    pass

def initialize():
    pygame.mixer.pre_init(44100, -16, 2 ,512)
    pygame.init()
    pygame.mixer.init()