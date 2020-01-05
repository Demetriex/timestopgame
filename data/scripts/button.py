class Button(object):
    def __init__(self, text, font, default, hover, aa=0, background=None):
        super().__init__()
        self.default = font.render(text, aa, default, background)
        self.hover = font.render(text, aa, hover)
        self.surface = self.default
        self.rect = self.default.get_rect()

    def update(self, mkey, mouse_pos):
        m1, m2, m3 = mkey
        if self.rect.collidepoint(mouse_pos):
            self.surface = self.hover
            if m1:
                return True
        else:
            self.surface = self.default
