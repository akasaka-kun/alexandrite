from typing import Dict
import pygame
import numpy as np

import characters


class Player:

    def __init__(self, player_id, controller, character: characters.Character, pos, textures: Dict[str, pygame.Surface], hurtboxes: Dict[str, pygame.Rect], hitboxes: Dict[str, pygame.Rect], clip_box: pygame.Rect):
        self.player_id = player_id
        self.controller = controller
        self.character = character

        self.pos = pos  # todo spawn the player on a default pos based on its id
        self.vel = np.array([0, 0])

        self.state_queue = []
        self.grounded_states = ('idle',)

        self.textures = textures
        self.hurtboxes = hurtboxes
        self.hitboxes = hitboxes
        self.clip_box = clip_box

    def state_machine(self):
        if self.state != 'idle' and not self.controller.actions:
            self.state_queue[0] = 'idle'
        if self.state == 'idle':
            if 'right' in self.controller:
                self.state_queue[0] = 'right'
            elif 'left' in self.controller:
                self.state_queue[0] = 'left'

    def update_vel(self, delta_time):
        if self.state in self.grounded_states:
            # ground accel
            if self.state == 'right':
                self.vel = [min(self.vel[0] + self.character.ground_accel, +self.character.ground_max_speed), self.vel[1]]
            elif self.state == 'left':
                self.vel = [min(self.vel[0] - self.character.ground_accel, -self.character.ground_max_speed), self.vel[1]]
        else:
            # air accel
            if self.state == 'right':
                self.vel = [min(self.vel[0] + self.character.air_accel, +self.character.air_max_speed), self.vel[1]]
            elif self.state == 'left':
                self.vel = [min(self.vel[0] - self.character.air_accel, -self.character.air_max_speed), self.vel[1]]
            self.vel = [self.vel[0], min(self.vel[1] - self.character.fall_speed, -self.character.max_fall_speed)]  # gravity

    def update(self, delta_time):
        self.pos += self.vel  # todo collision checks

    @property
    def state(self):
        return self.state_queue[0]
