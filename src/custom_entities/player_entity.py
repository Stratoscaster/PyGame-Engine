import pygame
import pymunk
from base_entities.static_entity import StaticEntity
from tools.animation import AnimationGroup
from tools.entity_state import EntityStateGroup
import tools.color_list as colors
import tools.constants as c
from base_entities.character_entity import CharacterEntity
# A Character-Entity is a class that inherits DynamicEntity(StaticEntity(Sprite))
# A Character-Entity class has other game-related attributes such as health, ammo, walk speed, etc


class PlayerEntity(CharacterEntity):
    WALK_SPEED_NAME = 'WALK_SPEED'
    WALK_ACCEL_NAME = 'WALK_ACCEL'

    def __init__(self, image=pygame.Surface(c.MEDIUM_TILE_SIZE)):
        super(PlayerEntity, self).__init__(image)
        self.create_stat(self.WALK_SPEED_NAME, 250)
        self.create_stat(self.WALK_ACCEL_NAME, self.get_stat(self.WALK_SPEED_NAME) * 0.80)
        self.right_arrow_held = False
        self.left_arrow_held = False
        self.frames_right_arrow_held = 0
        self.frames_left_arrow_held = 0



    def user_input(self, input_command):
        # Stopping character on key release is just a bad idea
        # if input_command == c.RIGHT_ARROW:
        #     self.set_target_vel_x(self.get_stat(self.WALK_SPEED_NAME), self.get_stat(self.WALK_ACCEL_NAME))
        # if input_command == c.LEFT_ARROW:
        #     self.set_target_vel_x(-1 * self.get_stat(self.WALK_SPEED_NAME), self.get_stat(self.WALK_ACCEL_NAME))
        # if input_command == c.RIGHT_ARROW_RELEASE or input_command == c.LEFT_ARROW_RELEASE:
        #     self.set_target_vel_x(0.0, self.get_stat(self.WALK_ACCEL_NAME))
        max_speed = self.get_stat(self.WALK_SPEED_NAME)
        accel = self.get_stat(self.WALK_ACCEL_NAME)
        mouse_pos = pygame.mouse.get_pos()
        if isinstance(self.shape, pymunk.Shape):
            if input_command == c.LEFT_MOUSE_BTN:
                print('LMB')
                self.shape.body.apply_force_at_local_point((100, 100))





        if c.DEBUG_PLAYER_INPUTS:
            print(input_command)

