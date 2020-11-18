import pygame as pg

from data.scripts.bullet import Bullet
from data.scripts.timer import Timer


class Character(object):
    def __init__(self, sprite, bullet_sprite, bullet_group):
        self.sprite = sprite
        self.speed = 10
        self.player_pos = None
        self.bullet_group = bullet_group
        self.bullet_sprite = bullet_sprite
        self.bullet_timer = Timer()
        self.rate_of_fire = 0.3
        self.can_shoot = True
        self.get_location()

    def get_location(self):
        self.player_pos = self.sprite.rect.center

    def player_movement(self, key):
        l, r, u, d = (key[pg.K_a], key[pg.K_d], key[pg.K_w], key[pg.K_s])
        if l:
            self.sprite.rect.centerx -= self.speed
        if r:
            self.sprite.rect.centerx += self.speed
        if u:
            self.sprite.rect.centery -= self.speed
        if d:
            self.sprite.rect.centery += self.speed

    def shoot_bullets(self, tick, mkey, mouse_pos):
        m1, m2, m3 = mkey

        if m1 and self.bullet_timer.elapsed(tick, self.rate_of_fire) and self.can_shoot:
            bullet = Bullet(self.bullet_sprite, self.player_pos, mouse_pos)
            self.bullet_group.add(bullet)

    def update(self, tick, key, mkey, mouse_pos, group):
        self.get_location()
        self.player_movement(key)
        self.shoot_bullets(tick, mkey, mouse_pos)
