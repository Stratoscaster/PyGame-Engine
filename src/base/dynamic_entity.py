import pygame

from base.static_entity import StaticEntity
from tools.animation import AnimationGroup
from tools.entity_state import EntityStateGroup
import tools.color_list as colors
import tools.constants as c

# DynamicEntity is a class that inherits StaticEntity(Sprite)
# A DynamicEntity can have states and animations, however they are unaffected by user input

class DynamicEntity(StaticEntity):

    def __init__(self, physics_body=None, image=pygame.Surface(c.MEDIUM_TILE_SIZE)):
        super(DynamicEntity, self).__init__(physics_body, image)
        self.states = EntityStateGroup()
        self.animations = AnimationGroup()

    def update(self):
        self.update_animation()
        self.update_state()
        super(DynamicEntity, self).update()

    def update_state(self):
        pass

    def update_animation(self):
        pass