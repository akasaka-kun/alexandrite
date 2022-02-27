import inspect
import warnings
import pygame
import config


class Controller:
    instances = None

    def __init__(self, controller, controls, instances):
        self.controller = controller
        self.actions = {}
        self.controls = controls
        instances.append(self)


class Keyboard(Controller):
    instances = []

    default_controls = {
        pygame.K_a: 'left',
        pygame.K_d: 'right',
        pygame.K_s: 'down',
        pygame.K_w: 'up',
        pygame.K_SPACE: 'dash',
        pygame.K_LEFT: 'light',
        pygame.K_DOWN: 'medium',
        pygame.K_RIGHT: 'heavy',
        pygame.K_UP: 'fluid'
    }

    def __init__(self):
        super(Keyboard, self).__init__('Keyboard', Keyboard.default_controls, self.__class__.instances)

    def update(self):
        for k, c in self.controls.items():
            if pygame.key.get_pressed()[k]:
                state = self.actions.get(c, [False, 0])
                hold_time = state[1] + 1
                self.actions[c] = (bool(hold_time - 1), hold_time)
            elif self.actions.get(c, False):
                self.actions.pop(c)
