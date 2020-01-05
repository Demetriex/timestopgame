import pygame as pg
from data.scripts.timer import Timer


class Character(object):
    def __init__(self, sprite, bullet_sprite):
        self.sprite = sprite
        self.speed = 10
        self.player_pos = None
        self.bullet_sprite = bullet_sprite
        self.bullet_timer = Timer()
        self.rate_of_fire = 0.3
        self.can_shoot = True
        self.get_location()

    def get_location(self):
        self.player_pos = self.sprite.rect.center

    def player_movement(self, key):
        l, r, u, d = (key[pg.K_a], key[pg.K_d],
                      key[pg.K_w], key[pg.K_s])
        if l:
            self.sprite.rect.centerx -= self.speed
        if r:
            self.sprite.rect.centerx += self.speed
        if u:
            self.sprite.rect.centery -= self.speed
        if d:
            self.sprite.rect.centery += self.speed

    def shoot_bullets(self, tick, mkey, mouse_pos, group):
        m1, m2, m3 = mkey

        if m1 and self.bullet_timer.elapsed(tick, self.rate_of_fire)\
                and self.can_shoot:
            bullet = Bullet(self.bullet_sprite, self.player_pos, mouse_pos)
            group.add(bullet)

    def update(self, tick, key, mkey, mouse_pos, group):
        self.get_location()
        self.player_movement(key)
        self.shoot_bullets(tick, mkey, mouse_pos, group)


class Bullet(pg.sprite.Sprite):
    def __init__(self, image, initial_pos, mouse_pos):
        super(Bullet, self).__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = initial_pos
        self.speed = 20
        self.vx, self.vy = (
            pg.math.Vector2(mouse_pos) -
            pg.math.Vector2(initial_pos)
        ).normalize() * self.speed

    def update(self, container):
        if not container.contains(self.rect):
            self.kill()

        self.rect.centerx += self.vx
        self.rect.centery += self.vy
