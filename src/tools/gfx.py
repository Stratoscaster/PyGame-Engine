import pygame
import tools.constants as c
class GFX:
    def __init__(self):
        self.layer_0 = pygame.sprite.Group()
        self.layer_1 = pygame.sprite.Group()
        self.layer_2 = pygame.sprite.Group()
        self.layer_3 = pygame.sprite.Group()
        self.layer_4 = pygame.sprite.Group()
        self.layer_5 = pygame.sprite.Group()
        self.layer_6 = pygame.sprite.Group()
        self.layer_7 = pygame.sprite.Group()
        self.layer_8 = pygame.sprite.Group()
        self.layers = [self.layer_0,
                       self.layer_1,
                       self.layer_2,
                       self.layer_3,
                       self.layer_4,
                       self.layer_5,
                       self.layer_6,
                       self.layer_7,
                       self.layer_8]
        self.canvas = pygame.Surface(c.NATIVE_SIZE)

    def update(self):
        for layer in self.layers:
            layer.update()

    def get_sprite_layers(self):
        return self.layers

    def draw(self, display):
        self.canvas.fill(c.BG_COLOR)
        for layer in self.layers:
            layer.draw(self.canvas)

        if c.SCALE > 1:
            pygame.transform.scale(self.canvas, c.DISPLAY_SIZE, display)
        else:
            display.blit(self.canvas, c.DISPLAY_TOP_LEFT)
        pygame.display.update()

    def add(self, sprite, layer):
        self.layers[layer].add(sprite)

    def remove_sprite(self, sprite):
        for layer in self.layers:
            if layer.has(sprite):
                layer.remove(sprite)
                return

        print('gfx.remove_sprite() failed - sprite not in layers')

