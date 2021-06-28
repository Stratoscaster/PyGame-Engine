import pygame
import pymunk
import tools.constants as c
from tools.sprite_image_manager import SpriteImgManager

# Debug Vars #
DEBUG_SPRITE_DRAWING = True

# Debug Vars #


aspect_ratio = 16/9
base_display_height = 720
base_display_width = int(base_display_height * aspect_ratio)
print(base_display_width, base_display_height)
WIN = pygame.display.set_mode((base_display_width,base_display_height))
canvas = pygame.surface.Surface((base_display_width, base_display_height))
TOP_LEFT = (0,0)

game_running = True
clock = pygame.time.Clock()
FPS = 75
sprites = []
sprite_imgs = SpriteImgManager([c.PLAYER_SPRITE_NAME])
sprite_imgs.load_sprite_images()
# pymunk setup
space = pymunk.space.Space()
space.gravity = (0.0,0.0)
class PlayerSprite(pygame.sprite.Sprite):

    def  __init__(self, shape):
        super(PlayerSprite, self).__init__()
        self.shape = shape

def draw_window():
    canvas.fill((100,100,100))


    for sprite in sprites:
        if isinstance(sprite, pygame.sprite.Sprite) and isinstance(sprite.shape, pymunk.Shape):
            sprite.update()
            print(sprite.shape.body.position)
            canvas.blit(sprite.image, (int(sprite.shape.body.position.x), int(sprite.shape.body.position.y)))
            if DEBUG_SPRITE_DRAWING:
                outline_rect(canvas, sprite.rect)


    WIN.blit(canvas, TOP_LEFT)
    pygame.display.update()

def outline_rect(surface, rect, color=pygame.Color((0,255,0)), width=1):
    pygame.draw.line(canvas, color, rect.topleft, rect.topright, width=width)  # top of rect
    pygame.draw.line(canvas, color, rect.topright, rect.bottomright, width=width) # right of rect
    pygame.draw.line(canvas, color, rect.bottomleft, rect.bottomright, width=width) # bottom of rect
    pygame.draw.line(canvas, color, rect.topleft, rect.bottomleft, width=width) # left of rect





def create_poly_player():
    image = sprite_imgs.get_img(c.PLAYER_SPRITE_NAME)
    # TODO: Setup image scaling
    rect = pygame.Rect(0,0,image.get_width(),image.get_height())
    body = pymunk.Body(body_type=pymunk.Body.DYNAMIC, mass=1, moment=1)
    body.position = (WIN.get_width() // 2, WIN.get_height() //2)
    player_shape = pymunk.Poly(body=body, vertices=(rect.topleft, rect.topright, rect.bottomleft, rect.bottomright))


    player = PlayerSprite(player_shape)
    player.rect = rect
    player.image = image
    player.shape = player_shape
    add_shape_to_space(player_shape)

    return player

def add_shape_to_space(shape):
    if isinstance(shape, pymunk.Shape):
        space.add(shape.body, shape)
        print('shape init pos @', shape.body.position)

def update():
    for sprite in sprites:
        if isinstance(sprite, PlayerSprite) and isinstance(sprite.rect, pygame.Rect) and isinstance(sprite.shape, pymunk.Shape):
            sprite.rect.topleft = (int(sprite.shape.body.position.x), int(sprite.shape.body.position.y))


def main_game():
    player = create_poly_player()
    sprites.append(player)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        update()
        draw_window()
        clock.tick(FPS)
        space.step(1/FPS)


main_game() # run game loop

pygame.quit()
quit()