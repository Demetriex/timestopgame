import pygame as pg


class Bullet(pg.sprite.Sprite):
    def __init__(self, image, initial_pos, mouse_pos):
        super(Bullet, self).__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = initial_pos
        self.speed = 20
        self.vx, self.vy = (
            pg.math.Vector2(mouse_pos) - pg.math.Vector2(initial_pos)
        ).normalize() * self.speed

    def update(self, container):
        if not container.contains(self.rect):
            self.kill()

        self.rect.centerx += self.vx
        self.rect.centery += self.vy
