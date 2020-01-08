from data.scripts.timer import Countdown
from data.load import BulletSprites, EnemySprite


class StageSystem(object):
    def __init__(self, spawner):
        self.done = False
        self.enemy_count = 5
        self.stage = 1
        self.spawner = spawner
        self.banner_timer = Countdown()
        self.countdown_timer = Countdown()
        self.banner_timer.setup_countdown(1)
        self.countdown_timer.setup_countdown(3)
        self.init()

    def init(self):
        EnemySprite.empty()
        BulletSprites.empty()
        self.enemy_count = 5
        self.stage = 1
        self.banner_timer.reset_timer()
        self.countdown_timer.reset_timer()
        self.spawner(self.enemy_count)

    def update(self, tick, enemies):
        if enemies == 0:
            self.banner_timer.reset_timer()
            BulletSprites.empty()
            self.done = True
            self.stage += 1
            self.enemy_count = self.enemy_count + 1
            self.spawner(self.enemy_count)

        if self.countdown_timer.done and self.done:
            self.done = False
            self.countdown_timer.reset_timer()

        if self.banner_timer.done:
            self.countdown_timer.tick_timer(tick)

        self.banner_timer.tick_timer(tick)
