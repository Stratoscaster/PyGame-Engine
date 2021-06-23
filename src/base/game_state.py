import gc

from tools.gfx import GFX
from tools.audio import Audio
from tools.sprite_image_manager import SpriteImgManager
from base.player_entity import PlayerEntity
from base.player_entity import StaticEntity
from tools.physics_engine import PhysicsEngine
import tools.constants as c

import pymunk
class GameState:
    def __init__(self, persist, needed_sprite_names):
        self.sprite_manager = SpriteImgManager(needed_sprite_names)
        self.persist = persist
        self.physics = PhysicsEngine(self)
        self.gfx  = GFX()
        self.audio = Audio()
        self.actor = self
        self.is_controllable = False
        self.is_done = False

    def initialize_player(self, start_pos: tuple):
        self.player = PlayerEntity(image=self.sprite_manager.get_img(c.PLAYER_SPRITE_NAME))
        self.player.pos_x = start_pos[0]
        self.player.pos_y = start_pos[1]

        player_body = pymunk.Body(c.PLAYER_MASS, c.PLAYER_INERTIA, body_type=c.PLAYER_BODY_TYPE)
        player_body.position = self.player.get_pos()
        player_rect_verts = [self.player.rect.topleft, self.player.rect.topright, self.player.rect.bottomright,
                             self.player.rect.bottomleft]
        player_body_shape = pymunk.shapes.Poly(body=player_body, vertices=player_rect_verts)

        self.physics.add_object_to_space(player_body, player_body_shape)
        self.player.set_physics_shape(player_body_shape)


    def update(self):
        self.physics.update()
        self.gfx.update()

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