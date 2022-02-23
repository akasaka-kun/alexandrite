import sys

import pygame
from config import screen_size, screen_flags

pygame.init()

screen = pygame.display.set_mode(screen_size, screen_flags if screen_flags else 0)


def redraw_screen():
    pygame.display.update()


while True:

    for e in pygame.event.get():
        match e.type:
            case pygame.QUIT:
                # close out function
                sys.exit()

    redraw_screen()
