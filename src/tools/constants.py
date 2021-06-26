import os

import pygame.font
import pymunk
pygame.font.init()

# PYMUNK PHYSICS
    # Player Physics Characteristics
PLAYER_MASS = 1
PLAYER_INERTIA = 100
PLAYER_BODY_TYPE = pymunk.Body.KINEMATIC

    # Dirt Physics Characteristics
DIRT_MASS = 1
DIRT_INERTIA = 100
DIRT_BODY_TYPE = pymunk.Body.STATIC

# DEBUGGING CONSTANTS
DRAW_SPRITE_POSITIONS = False
DEBUG_PLAYER_INPUTS = False
DEBUG_SPRITE_SHAPE_POSITIONS = False

# User Input Info
# Keyboard
UP_ARROW = 'UP_ARROW'
DOWN_ARROW = 'DOWN_ARROW'
LEFT_ARROW = 'LEFT_ARROW'
RIGHT_ARROW = 'RIGHT_ARROW'

UP_ARROW_RELEASE = 'UP_ARROW_RELEASE'
DOWN_ARROW_RELEASE = 'DOWN_ARROW_RELEASE'
LEFT_ARROW_RELEASE = 'LEFT_ARROW_RELEASE'
RIGHT_ARROW_RELEASE = 'RIGHT_ARROW_RELEASE'

# Controller
A_BTN = 'A_BTN'
B_BTN = 'B_BTN'
X_BTN = 'X_BTN'
Y_BTN = 'Y_BTN'
START_BTN = 'START_BTN'
SELECT_BTN = 'SELECT_BTN'

A_BTN_RELEASE = 'A_BTN_RELEASE'
B_BTN_RELEASE = 'B_BTN_RELEASE'
X_BTN_RELEASE = 'X_BTN_RELEASE'
Y_BTN_RELEASE = 'Y_BTN_RELEASE'
START_BTN_RELEASE = 'START_BTN_RELEASE'
SELECT_BTN_RELEASE = 'SELECT_BTN_RELEASE'

# FONTS

DEBUG_FONT = pygame.font.SysFont('consolas', size=10)

# Display Constants
FULL_SCREEN = 0
SCALE = 2
FPS = 60
BG_COLOR = (30,25,30)

# Game States
SPLASH_SCREEN = 'SPLASH_SCREEN'
MAIN_MENU = 'MAIN_MENU'
CHARACTER_SELECT = 'CHARACTER_SELECT'
LEVEL_SELECT = 'LEVEL_SELECT'
LEVEL = 'LEVEL'
CUTSCENE = 'CUTSCENE'
GAME_STATES = [
                SPLASH_SCREEN,
                MAIN_MENU,
                CHARACTER_SELECT,
                LEVEL_SELECT,
                LEVEL,
                CUTSCENE
            ]
STARTING_STATE = GAME_STATES[0]

# Directory Info
DIR_GRAPHICS = '\\graphics\\'
DIR_FONTS = '\\fonts\\'
DIR_SOUNDS = '\\sounds\\'
DIR_MUSIC = '\\music\\'
GRAPHICS_FOLDER = DIR_GRAPHICS.replace('\\', '')
FONTS_FOLDER = DIR_FONTS.replace('\\', '')
SOUNDS_FOLDER = DIR_SOUNDS.replace('\\', '')
MUSIC_FOLDER = DIR_MUSIC.replace('\\', '')

# Tile Information
SMALL_TILE_SIZE = (8, 8)
MEDIUM_TILE_SIZE = (16, 16)
LARGE_TILE_SIZE = (32, 32)

# Sprite Image Names
PLAYER_SPRITE_NAME = 'player_sprite'
DIRT_32x32_SPRITE_NAME = 'dirt_32x32_sprite'

SPRITE_NAMES = []
SPRITE_NAMES.extend([
    PLAYER_SPRITE_NAME,
    DIRT_32x32_SPRITE_NAME
])



# NATIVE RESOLUTION SETTINGS
NATIVE_WIDTH = 480
NATIVE_HEIGHT = 270
NATIVE_SIZE = (NATIVE_WIDTH, NATIVE_HEIGHT)
NATIVE_HEIGHT_CENTER = NATIVE_HEIGHT // 2
NATIVE_WIDTH_CENTER = NATIVE_WIDTH // 2
NATIVE_CENTER = (NATIVE_WIDTH_CENTER, NATIVE_HEIGHT_CENTER)
NATIVE_TOP = 0
NATIVE_BOTTOM = NATIVE_HEIGHT
NATIVE_LEFT = 0
NATIVE_RIGHT = NATIVE_WIDTH
NATIVE_TOP_LEFT = (NATIVE_LEFT, NATIVE_TOP)
NATIVE_TOP_RIGHT = (NATIVE_WIDTH, NATIVE_TOP)
NATIVE_BOTTOM_RIGHT = (NATIVE_WIDTH, NATIVE_HEIGHT)
NATIVE_BOTTOM_LEFT = (NATIVE_LEFT, NATIVE_BOTTOM)
NATIVE_TOP_CENTER = (NATIVE_WIDTH_CENTER, NATIVE_TOP)
NATIVE_RIGHT_CENTER = (NATIVE_WIDTH, NATIVE_HEIGHT_CENTER)
NATIVE_BOTTOM_CENTER = (NATIVE_WIDTH_CENTER, NATIVE_HEIGHT)
NATIVE_LEFT_CENTER = (NATIVE_LEFT, NATIVE_HEIGHT_CENTER)

# DISPLAY INFORMATION SETTINGS
DISPLAY_WIDTH = NATIVE_WIDTH * SCALE
DISPLAY_HEIGHT = NATIVE_HEIGHT * SCALE
DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
DISPLAY_HEIGHT_CENTER = DISPLAY_HEIGHT // 2
DISPLAY_WIDTH_CENTER = DISPLAY_WIDTH // 2
DISPLAY_CENTER = (DISPLAY_WIDTH_CENTER, DISPLAY_HEIGHT_CENTER)
DISPLAY_TOP = 0
DISPLAY_BOTTOM = DISPLAY_HEIGHT
DISPLAY_LEFT = 0
DISPLAY_RIGHT = DISPLAY_WIDTH
DISPLAY_TOP_LEFT = (DISPLAY_LEFT, DISPLAY_TOP)
DISPLAY_TOP_RIGHT = (DISPLAY_WIDTH, DISPLAY_TOP)
DISPLAY_BOTTOM_RIGHT = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
DISPLAY_BOTTOM_LEFT = (DISPLAY_LEFT, DISPLAY_BOTTOM)
DISPLAY_TOP_CENTER = (DISPLAY_WIDTH_CENTER, DISPLAY_TOP)
DISPLAY_RIGHT_CENTER = (DISPLAY_WIDTH, DISPLAY_HEIGHT_CENTER)
DISPLAY_BOTTOM_CENTER = (DISPLAY_WIDTH_CENTER, DISPLAY_HEIGHT)
DISPLAY_LEFT_CENTER = (DISPLAY_LEFT, NATIVE_HEIGHT_CENTER)