import operator
import sys

import numpy
import pygame

import characters
import controllers
import player
import utilities
from config import screen_size, screen_flags, bg_color

pygame.init()

screen = pygame.display.set_mode(screen_size, screen_flags if screen_flags else 0)
clock = pygame.time.Clock()


def redraw_screen():
    screen.fill(bg_color)
    pygame.draw.rect(screen, (255, 0, 0), utilities.RectOp(test.clip_box, test.pos, operator.add))
    pygame.display.update()


test = player.Player(0, controllers.Keyboard(), characters.test_char, (0, 0), {}, {}, {}, pygame.Rect(0, 0, 10, 10))
while True:

    for e in pygame.event.get():
        match e.type:
            case pygame.QUIT:
                # close out function
                sys.exit()

    dtime = clock.tick(60)

    print(test.pos, utilities.RectOp(test.clip_box, test.pos, operator.add))
    test.update(dtime)

    redraw_screen()
