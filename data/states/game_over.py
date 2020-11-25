import sys

import pygame as pg

from data.load import *
from data.scripts.button import Button
from data.scripts.state_machine import State


class GameOver(State):
    def __init__(self):
        super().__init__()
        self.background = BLACK
        self.new_game = Button("New Game", MEDIUM_FONT, WHITE, LIGHTBLUE)
        self.quit = Button("Quit", MEDIUM_FONT, WHITE, RED)
        self.next = "SPLASH"
        self.alpha = 0
        self.rate = 5
        self.background = pg.Surface(SCREEN_RECT.size)
        self.background.fill(BLACK)

    def cleanup(self):
        self.alpha = 0
        self.done = False
        return self.persistent

    def set_rect(self):
        self.quit.rect.midtop = CENTER
        self.new_game.rect.midbottom = CENTER

    def update(self, tick, keys, mkeys, mouse_pos):
        self.set_rect()
        self.alpha = min(self.alpha + self.rate, 255)
        self.background.set_alpha(self.alpha)
        if self.new_game.update(mkeys, mouse_pos):
            self.done = True
        if self.quit.update(mkeys, mouse_pos):
            sys.exit()

    def draw(self, surface):
        surface.blit(self.background, TOPLEFT)
        surface.blit(self.new_game.surface, self.new_game.rect)
        surface.blit(self.quit.surface, self.quit.rect)
