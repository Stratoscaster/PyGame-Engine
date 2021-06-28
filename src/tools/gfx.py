import pygame
import tools.color_list as color_list
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
            for sprite in layer:
                layer.draw(self.canvas)

            if c.DRAW_SPRITE_POSITIONS:
                for sprite in layer:
                    sprite_circle = pygame.draw.circle(self.canvas, color=(0, 255, 0), center=(sprite.rect.x, sprite.rect.y), radius=1)
                    if sprite_circle.collidepoint(pygame.mouse.get_pos()[0] / c.SCALE, pygame.mouse.get_pos()[1]/c.SCALE):
                        print('sprite rect pos:',sprite.rect.topleft)

        if c.DRAW_SPRITE_POSITIONS:
            sprite_draw_pos_text = c.DEBUG_FONT.render('rect positions drawn', True, color_list.GREEN, color_list.BLACK)
            self.canvas.blit(sprite_draw_pos_text, c.NATIVE_TOP_LEFT)


        # Leave scaling and display update at end of draw method
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

