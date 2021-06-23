import pygame

from base.static_entity import StaticEntity
from tools.animation import AnimationGroup
from tools.entity_state import EntityStateGroup
import tools.color_list as colors
import tools.constants as c
from base.dynamic_entity import DynamicEntity

# A Character-Entity is a class that inherits DynamicEntity(StaticEntity(Sprite))
# A Character-Entity class has other game-related attributes such as health, ammo, walk speed, etc

class CharacterEntity(DynamicEntity):

    def __init__(self, physics_body=None, image=pygame.Surface(c.MEDIUM_TILE_SIZE)):
        super(CharacterEntity, self).__init__(physics_body, image)
        self.stats = {} # Would hold health, ammo, speed, etc

    def create_stat(self, name, value=None):
        self.stats[name] = value

    def delete_stat(self, name):
        last_value = self.stats.pop(name)
        return last_value

    def change_stat(self, name, new_value):
        self.stats[name] = new_value

    def get_stat(self, name):
        return self.stats[name]

    def user_input(self, input_command):
        pass