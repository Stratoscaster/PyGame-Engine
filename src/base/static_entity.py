import pygame
import tools.constants as c
import tools.color_list as colors
from tools.physics_engine import PhysicsEngine
import pymunk
# StaticEntity is a class that inherits Sprite
# StaticEntity would represent something that can only move, and nothing else. It would not have game-based mechanics such as health, etc
# StaticEntity cannot be controlled by the player
# StaticEntities do not have animations or states

class StaticEntity(pygame.sprite.Sprite):
    def __init__(self, physics_shape=None, image=pygame.Surface(c.MEDIUM_TILE_SIZE)):
        super(StaticEntity, self).__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.pos_x = 0.0
        self.pos_y = 0.0
        self.vel_x = 0.0
        self.vel_y = 0.0

        self.physics_engine_set = False
        self.physics_shape = physics_shape

    def update(self):
        self.update_vel()
        self.update_pos()
        print(self.pos_x, self.pos_y)

    def set_physics_engine(self, physics_engine: PhysicsEngine):
        self.physics_engine_set = True
        self.physics_engine = physics_engine

    def set_physics_shape(self, shape: pymunk.Shape):
        self.physics_shape = shape

    def update_vel(self):
        pass

    def update_pos(self):
        if self.physics_shape is not None and isinstance(self.physics_shape, pymunk.Shape):
            self.pos_x = self.physics_shape.body.position[0]
            self.pos_y = self.physics_shape.body.position[1]
            self.rect.x = self.pos_x
            self.rect.y = self.pos_y
        else:
            pass

    #####################
    # Getters & Setters #
    #####################

    def set_pos(self, xy):
        self.pos_x = xy[0]
        self.pos_y = xy[1]

    def get_pos(self):
        return (self.pos_x, self.pos_y)

    def update_dt_frame_scaling(self, dt):
        self.dt = dt

    def set_vel_x(self, velocity):
        self.vel_x = velocity

    def set_vel_y(self, velocity):
        self.vel_y = velocity

    def get_velocity_vector(self):
        return (self.vel_x, self.vel_y)

    def set_acc_x(self, acceleration):
        self.acc_x = acceleration

    def set_acc_y(self, acceleration):
        self.acc_y = acceleration

    def set_target_vel_x(self, target_vel_x, acc_x=None, stay_on_target_vel_x=False):
        if acc_x is None:
            acc_x = self.acc_x
        self.target_vel_x = target_vel_x
        self.acc_x = abs(acc_x)
        self.target_vel_x_active = True
        self.stay_on_target_vel_x = stay_on_target_vel_x

    def set_target_vel_y(self, target_vel_y, acc_y=None, stay_on_target_vel_y=False):
        if acc_y is None:
            acc_y = self.acc_y
        self.target_vel_y = target_vel_y


        self.acc_y = abs(acc_y)
        self.target_vel_y_active = True
        self.stay_on_target_vel_y = stay_on_target_vel_y

    def unset_target_vel_x(self):
        self.target_vel_x_active = False
        self.stay_on_target_vel_x = False

    def unset_target_vel_y(self):
        self.target_vel_y_active = False
        self.stay_on_target_vel_y = False


    def unset_target_vel(self):
        self.unset_target_vel_x()
        self.unset_target_vel_y()




