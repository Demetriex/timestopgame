import pygame as pg


class AnimatedSprite(pg.sprite.Sprite):
    def __init__(self, images, position, fps):
        super(AnimatedSprite, self).__init__()
        self.images = images
        self.fps = fps
        self.timer = 0
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = position

    def update(self, now):
        self.timer += now
        if self.timer > 1000 / self.fps:
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
            self.timer = 0
