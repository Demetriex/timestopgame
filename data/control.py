import sys
import pygame as pg
from data.defaults import *
from data.load import *
from data.scripts.state_machine import StateMachine


class Control(object):
    def __init__(self):
        self.screen = SCREEN
        self.clock = pg.time.Clock()
        self.tick = 0
        self.keys = pg.key.get_pressed()
        self.mkeys = pg.mouse.get_pressed()
        self.screen_rect = self.screen.get_rect()
        self.mouse_pos = pg.mouse.get_pos()
        self.state_machine = StateMachine()

    def draw(self):
        if not self.state_machine.state.done:
            self.state_machine.state.draw(self.screen)

    def update(self):
        self.state_machine.update(self.tick, self.keys, self.mkeys, self.mouse_pos)

    def get_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self.keys = pg.key.get_pressed()
            elif event.type == pg.KEYUP:
                self.keys = pg.key.get_pressed()
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.mkeys = pg.mouse.get_pressed()
            elif event.type == pg.MOUSEBUTTONUP:
                self.mkeys = pg.mouse.get_pressed()
            self.mouse_pos = pg.mouse.get_pos()

    def run(self):
        self.playing = True
        while self.playing:
            self.tick = self.clock.tick(FPS)
            self.get_events()
            self.update()
            self.draw()
            pg.display.flip()
