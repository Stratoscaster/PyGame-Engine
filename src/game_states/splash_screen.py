from game_states.game_state import GameState
import tools.constants as c


class SplashScreen(GameState):

    def __init__(self, persists = None):
        needed_sprites = [c.PLAYER_SPRITE_NAME, c.DIRT_32x32_SPRITE_NAME, c.RED_ENEMY_SPRITE_NAME]
        super(SplashScreen, self).__init__(persists, needed_sprites)
        self.is_controllable = True

        self.initialize_player()
        self.initialize_enemies()



        self.add_sprite(self.player, 4)
        self.set_actor(self.player)



    def add_sprite(self, sprite, layer):
        super(SplashScreen, self).add_sprite(sprite, layer)

    def update(self):
        super(SplashScreen, self).update()
        self.player.update()

    def initialize_player(self):
        return super(SplashScreen, self).initialize_player()

    def initialize_enemies(self):
        num_enemies_to_init = 100
        self.enemies = [self.initialize_enemy() for i in range(0,num_enemies_to_init)]
        for enemy in self.enemies:
            self.add_sprite(enemy, 4)

