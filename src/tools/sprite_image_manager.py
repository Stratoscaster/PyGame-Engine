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
        self.sprite_img_paths[name] = path
        img = pygame.image.load(self.sprite_img_paths[name])
        self.sprite_img_list[name] = img
        return self.sprite_img_list[name]


    # Add new sprites here so they can be used
    # can also add custom sprite paths to constants python file
    def load_sprite_paths(self):
        # path_example = os.path.join('src','graphics', 'your_sprite_image_here.png')

        sprite_paths = c.SPRITE_PATHS

        return sprite_paths

    def load_sprite_images(self):
        # TODO: determine if best practice would be to keep *all* sprite
        #  imgs loaded, or to load them on game state flip. Would optimization be necessary even?
        sprite_images = {}
        for sprite_name in self.sprite_img_paths.keys():
            if sprite_name in self.needed_sprite_images:
                img = pygame.image.load(self.sprite_img_paths[sprite_name]).convert_alpha()
                # img = pygame.Surface.convert_alpha(img)
                sprite_images[sprite_name] = img

        return sprite_images



    def get_img(self, name):
        if name in self.sprite_img_list.keys():
            return self.sprite_img_list[name]
        else:
            raise SpriteImageNotLoadedException('The following sprite was attempted to be retrieved but was not loaded into memory: ' + name)

    def get_scaled_img(self, name: str, scale=(c.SCALE,c.SCALE)):
        if name in self.sprite_img_list.keys():
            scaled_img = pygame.transform.scale(self.sprite_img_list[name], scale)
            return scaled_img

    def reload_img(self, sprite_name):
        if sprite_name in self.needed_sprite_images and sprite_name in self.sprite_img_paths:
            img = pygame.image.load(self.sprite_img_paths[sprite_name])
            self.sprite_img_list[sprite_name] = img
        else:
            raise SpriteImageNotLoadedException('sprite name found in needed sprite images = '
                                                + str(sprite_name in self.needed_sprite_images)
                                                + '. sprite name found in sprite image paths = '
                                                + str(sprite_name in self.sprite_img_paths))

class SpriteImageNotLoadedException(Exception):

    def __init__(self, error):
        self.msg = error