import pygame
from pip._internal.utils.deprecation import deprecated

import tools.constants as c
import tools.color_list as colors
from tools.physics_engine import PhysicsEngine
import pymunk
# StaticEntity is a class that inherits Sprite
# StaticEntity would represent something that can only move, and nothing else. It would not have game-based mechanics such as health, etc
# StaticEntity cannot be controlled by the player
# StaticEntities do not have animations or states


class StaticEntity(pygame.sprite.Sprite):
    def __init__(self, image=pygame.Surface(c.MEDIUM_TILE_SIZE)):
        super(StaticEntity, self).__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.pos_x = 0.0
        self.pos_y = 0.0
        self.vel_x = 0.0
        self.vel_y = 0.0

        self.physics_engine_set = False
        self.physics_engine = None
        self.physics_shape = None

    def update(self):
        self.update_vel()
        self.update_pos()
        if c.DEBUG_SPRITE_SHAPE_POSITIONS:
            print('')
            print('sprite pos:', self.pos_x, self.pos_y)
            print('rect pos:', self.rect.x, self.rect.y)
            if isinstance(self.physics_shape, pymunk.Shape):
                print('!physics_shape_pos', self.physics_shape.body.position[0], self.physics_shape.body.position[1])
                print('!physics_shape_force', self.physics_shape.body.force)
                print('!physics_shape_velocity', self.physics_shape.body.velocity)



    def set_physics_engine(self, physics_engine: PhysicsEngine):
        self.physics_engine_set = True
        self.physics_engine = physics_engine

    def set_physics_shape(self, shape: pymunk.Shape):
        self.physics_shape = shape

    def create_set_get_physics_shape(self, entity_mass, entity_inertia, entity_body_type):
        entity_body = pymunk.Body(entity_mass, entity_inertia, entity_body_type)
        entity_body.position = (self.pos_x, self.pos_y)
        entity_rect_verts = [self.rect.topleft, self.rect.topright, self.rect.bottomright, self.rect.bottomleft]
        entity_shape = pymunk.shapes.Poly(body=entity_body, vertices=entity_rect_verts)
        self.set_physics_shape(entity_shape)
        self.physics_engine.add_object_to_space(entity_shape.body, entity_shape)
        return entity_shape

    def update_vel(self):
        pass

    #[DONE] TODO: Update to use pymunk instead of manually changing pos_x and updating rect.x (etc)
    #TODO: gfx's rect position not matching pymunk?
    def update_pos(self):
        if isinstance(self.physics_shape, pymunk.Shape):
            self.pos_x = int(self.physics_shape.body.position[0])
            self.pos_y = int(self.physics_shape.body.position[1])
            self.rect.topleft = tuple((int(self.physics_shape.body.position[0]), int(self.physics_shape.body.position[1])))
        else:
            print('No physics shape for static entity.')




    #####################
    # Getters & Setters #
    #####################

    def set_pos(self, xy):
        self.set_pos_x(xy[0])
        self.set_pos_y(xy[1])
        if isinstance(self.physics_shape, pymunk.Shape):
            self.physics_shape.body.position = xy

    def set_pos_x(self, x):
        self.pos_x = x
        self.rect.centerx = int(x)
        # if isinstance(self.physics_shape, pymunk.Shape):
        #     self.physics_shape.body.position[0] = x

    def set_pos_y(self, y):
        self.pos_y = y
        self.rect.centery = int(self.pos_y)
        # if isinstance(self.physics_shape, pymunk.Shape):
        #     self.physics_shape.body.position[1] = y

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




