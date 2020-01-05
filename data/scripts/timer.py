class Timer(object):
    def __init__(self):
        self.start_time = 0
        self.now = 0

    def elapsed(self, tick, time=1):
        if self.now - self.start_time >= 1000 * time:
            self.start_time = self.now
            return True
        self.now += tick


class Countdown(object):
    def __init__(self):
        self.timer = Timer()
        self.seconds = None
        self.number = None
        self.done = False

    def setup_countdown(self, seconds):
        self.seconds = seconds
        self.number = seconds

    def tick_timer(self, tick):
        if self.number >= 0:
            if self.timer.elapsed(tick):
                self.number += -1
        else:
            self.done = True

    def reset_timer(self):
        self.number = self.seconds
        self.done = False
