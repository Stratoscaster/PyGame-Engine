import gc

from tools.gfx import GFX
from tools.audio import Audio
from tools.sprite_image_manager import SpriteImgManager
from base.player_entity import PlayerEntity
from base.player_entity import StaticEntity
from tools.physics_engine import PhysicsEngine
class GameState:
    def __init__(self, persist, needed_sprite_names):
        self.sprite_manager = SpriteImgManager(needed_sprite_names)
        self.persist = persist
        self.physics = PhysicsEngine()
        self.gfx  = GFX()
        self.audio = Audio()
        self.actor = self
        self.is_controllable = False
        self.is_done = False

    def update(self):
        self.gfx.update()
        self.detect_collisions()

    def draw(self, display):
        self.gfx.draw(display)

    def add_sprite(self, sprite, layer):
        self.gfx.add(sprite, layer)
        self.physics.add_sprite(sprite)

    def cleanup(self):
        self.is_done = False

    def flip_state(self, state):
        self.is_done = True
        self.next_state = state

    def user_input(self, input_command):
        if self.is_controllable:
            pass
# Getters & Setters

    def set_actor(self, actor):
        self.actor = actor

    def get_actor(self):
        return self.actor