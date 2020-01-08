import random
import pygame as pg
from data.scripts.mobs import Mobs
from data.scripts.timer import Timer, Countdown
from data.scripts.state_machine import State
from data.scripts.stage import StageSystem
from data.scripts.skill import Skill
from data.load import *


class Game(State):
    def __init__(self):
        super().__init__()
        self.background = GRAY
        self.player_hp = 3
        self.timer = Timer()
        self.countdown_timer = Countdown()
        self.countdown_timer.setup_countdown(3)
        self.timestop = Skill(10, 2, pg.K_SPACE)
        self.stage = StageSystem(self.spawn_enemies)
        self.stage.init()
        self.playing = True
        self.next = "GAMEOVER"

    def cleanup(self):
        self.done = False
        self.player_hp = 3
        self.playing = True
        self.stage.init()
        self.persistent.sprite.rect.center = CENTER
        self.countdown_timer.reset_timer()
        self.timestop.reinit()

        return self.persistent

    def update(self, tick, keys, mkeys, mouse_pos):
        if not self.stage.countdown_timer.done\
                or not self.stage.banner_timer.done:
            self.persistent.can_shoot = False
        else:
            self.persistent.can_shoot = True
        if self.playing:
            if self.stage.countdown_timer.done:
                self.hits()
                if not self.timestop.skill_used:
                    EnemySprite.update(tick, self.persistent.player_pos)
                    BulletSprites.update(SCREEN_RECT)

            self.persistent.update(tick, keys, mkeys, mouse_pos, BulletSprites)
            self.persistent.sprite.rect.clamp_ip(SCREEN_RECT)
            PlayerSprite.update(tick)
        else:
            self.done = True

        self.timestop.update(tick, keys)
        self.stage.update(tick, len(EnemySprite))
        self.check_hp()

    def draw(self, surface):
        surface.fill(self.background)
        PlayerSprite.draw(surface)
        EnemySprite.draw(surface)
        BulletSprites.draw(surface)
        self.render_countdown_timer(surface)
        self.render_stage_complete(surface)
        self.render_skill_usage(surface)
        self.render_hp(surface)

    def hits(self):
        hits = pg.sprite.groupcollide(EnemySprite, PlayerSprite,
                                      True, False)
        pg.sprite.groupcollide(EnemySprite, BulletSprites, True, True)

        self.player_hp = self.player_hp - len(hits)

    def spawn_enemies(self, number):
        for x in range(number):
            monster = random.choice(
                [SPRITES["redmonster"], SPRITES["slime"]]
            )
            rand_num = random.randrange(WIDTH)
            EnemySprite.add(Mobs(monster, (rand_num, -100), 12))

    def render_hp(self, surface):
        hp = SMALL_FONT.render(
            "HP: " + str(self.player_hp), 0, BLACK
        )
        surface.blit(hp, hp.get_rect(topleft=TOPLEFT))

    def render_countdown_timer(self, surface):
        if self.stage.countdown_timer.number >= 0\
                and not self.countdown_timer.done\
                and self.stage.banner_timer.done:

            text = str(self.stage.countdown_timer.number)
            if text == "0":
                text = "Start!"
            number = BIG_FONT.render(text, 0, RED)
            surface.blit(
                number,
                number.get_rect(center=CENTER)
            )

    def render_stage_complete(self, surface):
        if not self.stage.banner_timer.done:
            stage_complete = MEDIUM_FONT.render(
                "Stage " + str(self.stage.stage), 0, RED
            )
            surface.blit(
                stage_complete,
                stage_complete.get_rect(center=CENTER)
            )

    def render_skill_usage(self, surface):
        if self.timestop.on_cooldown:
            text = "Skill in Cooldown"
        else:
            text = "Skill Ready"
        message = SMALL_FONT.render(text, 0, BLACK)
        surface.blit(message, message.get_rect(topright=TOPRIGHT))

    def check_hp(self):
        if self.player_hp <= 0:
            self.playing = False
