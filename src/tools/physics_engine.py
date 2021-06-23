from base.static_entity import StaticEntity
import pygame
class PhysicsEngine:

    def __init__(self, game_state):
        self.sprites = []
        self.dt = 1

    def add_sprite(self, sprite):
        if isinstance(sprite, StaticEntity):
            sprite.set_physics_engine(self)
            self.sprites.append(sprite)
        else:
            print('PhysicsEngine could not add object as sprite. Object was of type: ' + type(sprite))

    def check_collisions(self, sprite_source):
        collided_rects = self.detect_collision(sprite_source)
        collision_types = {'top':False, 'bottom':False, 'left':False, 'right':False}
        test_rect = pygame.Rect(sprite_source.Rect)



    def detect_collision(self, sprite_source):
        collided_rects = []
        for sprite_target in self.sprites:
            if isinstance(sprite_target, StaticEntity) and isinstance(sprite_source, StaticEntity) and sprite_target != sprite_source:
                target_rect = sprite_target.rect
                source_rect = sprite_source.rect
                if isinstance(target_rect, pygame.Rect) and isinstance(source_rect, pygame.Rect):
                    if source_rect.colliderect(target_rect):
                        collided_rects.append(target_rect)

        return collided_rects

    def calc_next_movement(self, sprite):
        movement_calculation = {'x':None, 'y':None, 'x_vel':None, 'y_vel':None, 'x_acc':None, 'y_acc':None}
        pass
        return movement_calculation

    def calc_next_velocity(self, sprite):
        pass

    def calc_next_position(self, sprite):
        pass

    def get_sprite_rects(self):
        rects = [sprite.rect for sprite in self.sprites]

    def update_dt_frame_scaling(self, dt):
        self.dt = dt

class CollisionDetection:

    def __init__(self, source, targets: list):
        self.targets = targets
        if isinstance(source, StaticEntity):
            self.source = source
        else:
            print(f'CollisionDetection expects StaticEntity-inherited classes. (source) was type ({type(source)})')







