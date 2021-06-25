import pymunk

from base.game_state import GameState
from base.character_entity import CharacterEntity
from base.player_entity import PlayerEntity
from base.static_entity import StaticEntity
import tools.constants as c

class SplashScreen(GameState):

    def __init__(self, persists = None):
        needed_sprites = [c.PLAYER_SPRITE_NAME, c.DIRT_32x32_SPRITE_NAME]
        super(SplashScreen, self).__init__(persists, needed_sprites)
        # Add Dirt ground
        self.dirt_sprites = []
        num_dirt_layers = 2
        for j in range(0, num_dirt_layers):
            for i in range(0, c.DISPLAY_HEIGHT // 32):
                dirt = StaticEntity(image=self.sprite_manager.get_img(c.DIRT_32x32_SPRITE_NAME))
                dirt.set_pos((i * 32 , c.NATIVE_HEIGHT - (32 * (j + 1))))
                dirt.set_physics_engine(self.physics)
                dirt.create_set_get_physics_shape(c.DIRT_MASS, c.DIRT_INERTIA, c.DIRT_BODY_TYPE)
                self.dirt_sprites.append(dirt)
                self.add_sprite(dirt, 3)

        # Calculate ground height, init player
        ground_y = c.NATIVE_HEIGHT - (32 * (num_dirt_layers))

        self.initialize_player((100, ground_y))

        self.add_sprite(self.player, 4)
        self.set_actor(self.player)



    def add_sprite(self, sprite, layer):
        super(SplashScreen, self).add_sprite(sprite, layer)

    def update(self):
        super(SplashScreen, self).update()
        self.player.update()

