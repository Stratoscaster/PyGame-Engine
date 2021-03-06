import pygame
import pymunk
import tools.constants as c
from pymunk.shapes import Shape
class PhysicsEngine:

    def __init__(self, game_state):
        self.game_state = game_state
        self.sprites = []
        self.dt = 1
        self.space = pymunk.Space()
        self.space.gravity = (0 , 100)

    def add_sprite(self, sprite):
        from base.static_entity import StaticEntity
        if isinstance(sprite, StaticEntity):
            sprite.set_physics_engine(self)
            self.sprites.append(sprite)
        else:
            print('PhysicsEngine could not add object as sprite. Object was of type: ' + type(sprite))

    def update(self):
        self.update_simulation()

    def update_simulation(self):
        if self.dt != 0:
            current_fps = c.FPS * self.dt
            seconds_to_simulate = 1 / current_fps
            number_of_steps = 10

            for step in range(0, number_of_steps):
                self.space.step(seconds_to_simulate / number_of_steps)

    def add_object_to_space(self, body, shape):
        self.space.add(body, shape)

    def update_dt_frame_scaling(self, dt):
        self.dt = dt

    def force_sprite(self, sprite, force_vector: tuple):
        from base.static_entity import StaticEntity
        if isinstance(sprite, StaticEntity):
            if isinstance(sprite.physics_shape, pymunk.Shape):
                sprite.physics_shape.body.apply_force_at_local_point(force_vector, sprite.rect.center)



class CollisionDetection:

    def __init__(self, source, targets: list):
        pass
        # self.targets = targets
        # if isinstance(source, StaticEntity):
        #     self.source = source
        # else:
        #     print(f'CollisionDetection expects StaticEntity-inherited classes. (source) was type ({type(source)})')







