from tools.gfx import GFX
from tools.audio import Audio
from tools.sprite_image_manager import SpriteImgManager
from custom_entities.player_entity import PlayerEntity
from custom_entities.enemy_entity import EnemyEntity
from tools.physics_engine import PhysicsEngine
import tools.constants as c
import random
import pymunk
from time import sleep
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
        self.freeze_frame_debug = False

    def initialize_player(self):
        self.player = PlayerEntity(image=self.sprite_manager.get_img(c.PLAYER_SPRITE_NAME))
        self.player.set_pos((0,0))
        self.player.set_physics_engine(self.physics)
        self.player.create_set_get_physics_shape(c.PLAYER_MASS, c.PLAYER_INERTIA, c.PLAYER_BODY_TYPE)
        self.player.shape.elasticity = 0.3

    def initialize_enemy(self, color=None, starting_pos=None, mass=c.PLAYER_MASS,
                          inertia=c.PLAYER_INERTIA, body_type=pymunk.Body.DYNAMIC, elasticity=1):
        enemy = EnemyEntity(color=color, image=self.sprite_manager.get_img(c.RED_ENEMY_SPRITE_NAME))
        # TODO: replace enemy position determination with actual spawning procedure
        if starting_pos is None:
            enemy.set_pos((random.uniform(0, c.DISPLAY_WIDTH -32), random.uniform(0, c.DISPLAY_HEIGHT -32)))
        else:
            enemy.set_pos(starting_pos)

        enemy.set_physics_engine(self.physics)
        enemy.create_set_get_physics_shape(entity_mass=mass, entity_inertia=inertia,
                                                   entity_body_type=body_type, elasticity=elasticity)
        return enemy


    def update(self):
        self.check_freeze_frame_debug()
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
        if self.is_controllable and c.DEBUG_SLEEP_MODE:
            if input_command == c.FREEZE_FRAME_KEY:
                self.freeze_frame_debug = True

    def check_freeze_frame_debug(self):
        if self.freeze_frame_debug:
            sleep(2)
            self.freeze_frame_debug = False

# Getters & Setters

    def set_actor(self, actor):
        self.actor = actor

    def get_actor(self):
        return self.actor