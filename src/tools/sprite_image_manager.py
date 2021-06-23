import os
import pygame
import tools.constants as c
class SpriteImgManager():

    def __init__(self, needed_sprite_images: list):
        self.needed_sprite_images = needed_sprite_images
        self.sprite_img_paths = self.load_sprite_paths()
        self.sprite_img_list = self.load_sprite_images()
        self.custom_sprites = {}

    def add_sprite_img(self, name: str, path: os.path):
        pass
    # Add new sprites here so they can be used
    def load_sprite_paths(self):
        # path_test = os.path.join('src','graphics', 'player_v1.png')
        # print(path_test)
        # print(os.path.abspath(path_test))

        sprite_paths = {
            c.PLAYER_SPRITE_NAME : os.path.join('src','graphics', 'player_v1.png'),
            c.DIRT_32x32_SPRITE_NAME : os.path.join('src', 'graphics', 'dirt_32x32.png')
        }

        return sprite_paths

    def load_sprite_images(self):
        sprite_images = {}
        for sprite_name in self.sprite_img_paths.keys():
            if sprite_name in self.needed_sprite_images:
                img = pygame.image.load(self.sprite_img_paths[sprite_name])
                sprite_images[sprite_name] = img

        return sprite_images


    def get_img(self, name):
        if name in self.sprite_img_list.keys():
            return self.sprite_img_list[name]
        else:
            raise SpriteImageNotLoadedException('The following sprite was attempted to be retrieved but was not loaded into memory: ' + name)

class SpriteImageNotLoadedException(Exception):

    def __init__(self, error):
        self.msg = error