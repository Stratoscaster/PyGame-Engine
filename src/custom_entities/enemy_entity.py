import pymunk
import pygame
from base_entities.character_entity import CharacterEntity
from tools.physics_engine import PhysicsEngine
import random
import tools.constants as c
import numpy as np
class EnemyEntity(CharacterEntity):


    def __init__(self, color=None, image = pygame.Surface(c.MEDIUM_TILE_SIZE)):
        super(EnemyEntity, self).__init__()
        self.image = image
        if color is None:
            self.color = tuple([int(random.triangular(0,255,100)) for i in range(0,3)])


    def update(self):
        super(EnemyEntity, self).update()


    def create_set_get_physics_shape(self, entity_mass, entity_inertia, entity_body_type, elasticity:int = None):
        entity_body = pymunk.Body(entity_mass, entity_inertia,  entity_body_type)
        entity_body.position = (self.pos_x, self.pos_y)
        entity_shape = pymunk.shapes.Circle(body=entity_body, radius=20)
        if elasticity is not None:
            entity_shape.elasticity = elasticity
        self.set_physics_shape(entity_shape)
        if isinstance(self.physics_engine, PhysicsEngine):
            self.physics_engine.add_object_to_space(entity_shape.body, entity_shape)


        return entity_shape

