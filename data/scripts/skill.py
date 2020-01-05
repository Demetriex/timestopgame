from data.scripts.timer import Countdown


class Skill(object):
    def __init__(self, cooldown, duration, key):
        self.duration = duration
        self.cooldown = cooldown
        self.key = key
        self.on_cooldown = False
        self.skill_used = False
        self.cooldown_timer = Countdown()
        self.duration_timer = Countdown()
        self.cooldown_timer.setup_countdown(self.cooldown)
        self.duration_timer.setup_countdown(self.duration)

    def reinit(self):
        self.on_cooldown = False
        self.skill_used = False
        self.cooldown_timer.reset_timer()
        self.duration_timer.reset_timer()

    def update(self, tick, keys):
        if not self.on_cooldown and keys[self.key]:
            self.skill_used = True
            self.on_cooldown = True

        if self.duration_timer.done:
            self.skill_used = False
            self.duration_timer.reset_timer()

        if self.cooldown_timer.done:
            self.on_cooldown = False
            self.cooldown_timer.reset_timer()

        self.duration_timer.tick_timer(tick)
        self.cooldown_timer.tick_timer(tick)
