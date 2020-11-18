import pygame as pg

from data.load import SCREEN_RECT, TOPLEFT


class MovingBackground(object):
    def __init__(self, image, sprite_group):
        self.sprite_group = sprite_group
        self.image = image
        self.speed = 3
        self.bg = Background(self.image, self.speed)
        self.init()

    def init(self):
        copy1 = self.bg.copy()
        copy2 = self.bg.copy()
        copy1.rect.topleft = TOPLEFT
        copy2.rect.bottomleft = TOPLEFT
        self.sprite_group.add(copy1)
        self.sprite_group.add(copy2)

    def update(self):
        self.sprite_group.update()
        if len(self.sprite_group) == 1:
            bg = self.bg.copy()
            bg.rect.bottomleft = TOPLEFT
            self.sprite_group.add(bg)


class Background(pg.sprite.Sprite):
    def __init__(self, image, speed):
        super(Background, self).__init__()
        self.speed = speed
        self.image = image
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += self.speed
        if self.rect.top >= SCREEN_RECT.bottom:
            self.kill()

    def copy(self):
        return Background(self.image, self.speed)
