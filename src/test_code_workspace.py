import os
import pygame
target = os.path.join('graphics', 'player_v1.png')
img = pygame.image.load(target)
print(type(img))