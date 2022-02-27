from typing import Dict

import numpy
import pygame
import numpy as np
from numpy import sign

import characters


class Player:
    STATE_IDLE = 'idle'
    STATE_WALK_RIGHT = 'walk right'
    STATE_WALK_LEFT = 'walk left'

    def __init__(self, player_id, controller, character: characters.Character, pos, textures: Dict[str, pygame.Surface], hurtboxes: Dict[str, pygame.Rect], hitboxes: Dict[str, pygame.Rect], clip_box: pygame.Rect):
        self.player_id = player_id
        self.controller = controller
        self.character = character

        self.pos = pos  # todo spawn the player on a default pos based on its id
        self.vel = np.array([0, 0])

        self.state_queue = []
        self.grounded_states = (Player.STATE_IDLE, Player.STATE_WALK_RIGHT, Player.STATE_WALK_LEFT)

        self.textures = textures
        self.hurtboxes = hurtboxes
        self.hitboxes = hitboxes
        self.clip_box = clip_box

    def state_machine(self):
        if self.state != Player.STATE_IDLE and not self.controller.actions:
            self.state_queue[0] = Player.STATE_IDLE
        if self.state == Player.STATE_IDLE:
            if 'right' in self.controller.actions:  # todo add a controls set to standardize controls between controllers
                self.state_queue[0] = Player.STATE_WALK_RIGHT
            elif 'left' in self.controller.actions:
                self.state_queue[0] = Player.STATE_WALK_LEFT

    def update_vel(self, delta_time):
        if self.state in self.grounded_states:
            # ground accel
            if self.state == Player.STATE_WALK_RIGHT:
                self.vel = [min(self.vel[0] + self.character.ground_accel / delta_time, +self.character.ground_max_speed), self.vel[1]]
            elif self.state == Player.STATE_WALK_LEFT:
                self.vel = [max(self.vel[0] - self.character.ground_accel / delta_time, -self.character.ground_max_speed), self.vel[1]]
            if self.state not in (Player.STATE_WALK_RIGHT, Player.STATE_WALK_LEFT):
                self.vel = [sign(self.vel[0]) * max(0.0, abs(self.vel[0]) - self.character.ground_decel / delta_time), self.vel[1]]
        else:
            # air accel
            if self.state == Player.STATE_WALK_RIGHT:
                self.vel = [min(self.vel[0] + self.character.air_accel / delta_time, +self.character.air_max_speed), self.vel[1]]
            elif self.state == Player.STATE_WALK_LEFT:
                self.vel = [max(self.vel[0] - self.character.air_accel / delta_time, -self.character.air_max_speed), self.vel[1]]
            self.vel = [self.vel[0], min(self.vel[1] - self.character.fall_speed / delta_time, -self.character.max_fall_speed)]  # gravity

    def update(self, delta_time):
        self.controller.update()
        self.state_machine()
        self.update_vel(delta_time)
        self.pos += numpy.asarray(self.vel)  # todo collision checks

    @property
    def state(self):
        try:
            return self.state_queue[0]
        except IndexError:
            self.state_queue.append(self.STATE_IDLE)
        return self.state_queue[0]
