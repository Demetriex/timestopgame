import random
from data.scripts.animated import AnimatedSprite


class Mobs(AnimatedSprite):
    def __init__(self, images, position, fps):
        super().__init__(images, position, fps)
        self.speed = random.randrange(3, 7)
        self.vx, self.vy = self.speed, self.speed

    def move_to(self, point):
        px, py = point
        cx, cy = self.rect.center
        if cy >= py:
            self.vy = -self.speed
        if cy <= py:
            self.vy = self.speed
        if cx >= px:
            self.vx = -self.speed
        if cx <= px:
            self.vx = self.speed

        self.rect.centerx += self.vx
        self.rect.centery += self.vy

    def update(self, now, point):

        self.timer += now
        if self.timer > 1000 / self.fps:
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
            self.timer = 0

        self.move_to(point)
