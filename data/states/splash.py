import pygame as pg

from data.load import *
from data.scripts.state_machine import State
from data.scripts.timer import Countdown


class Splash(State):
    _alpha = 0
    _rate = 10

    def __init__(self):
        super().__init__()
        self.background = WHITE
        self.ticks = 0
        self.splash = BIG_FONT.render(TITLE, 0, BLACK)
        self.any_key = SMALL_FONT.render("Press any key...", 0, BLACK)
        self.next = "GAME"

        self.timer = Countdown()
        self.timer.setup_countdown(1)

    def cleanup(self):
        self.done = False
        self.timer.reset_timer()

        return self.persistent

    def set_rect(self):
        self.splash_rect = self.splash.get_rect()
        self.splash_rect.center = CENTER
        self.any_key_rect = self.any_key.get_rect()
        self.any_key_rect.midtop = self.splash_rect.midbottom

    def update(self, tick, keys, mkeys, mouse_pos):
        self.set_rect()
        self.ticks += tick
        if not 0 <= self._alpha <= 255:
            self._rate = self._rate * -1
        self._alpha += self._rate
        self.any_key.set_alpha(self._alpha)
        if not self.timer.done:
            self.timer.tick_timer(tick)
        if (any(keys) or any(mkeys)) and self.timer.done:
            self.done = True

    def draw(self, surface):
        surface.fill(self.background)
        surface.blit(self.splash, self.splash_rect)
        surface.blit(self.any_key, self.any_key_rect)
