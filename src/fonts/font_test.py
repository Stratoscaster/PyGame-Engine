import pygame
import threading
from time import sleep
font_list = pygame.font.get_fonts()


pygame.font.init()
pygame.init()


while True:
    print('"quit!" to quit. type "font_list" to list fonts, or type a font to display it')
    user_input = input('>')

    if user_input == 'font_list':
        for font in font_list:
            print('-', font)
    elif user_input == 'quit!':
        break
    elif user_input in font_list:
        print('using',user_input)
        WIN = pygame.display.set_mode((720, 480))
        canvas = pygame.Surface((WIN.get_width(), WIN.get_height()))
        canvas.fill((0, 0, 0))
        user_font = pygame.font.SysFont(user_input, 20)
        font_rendered = user_font.render(user_input, True, (0,255,0), (0,0,0))
        canvas.blit(font_rendered, (0,0))
        WIN.blit(canvas, (0, 0))
        pygame.display.update()
        sleep(15)
        pygame.display.quit()

    else:
        print('font not in list!')
