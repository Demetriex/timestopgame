class StatSystem(object):
    def __init__(self, stats):
        self.stats = stats
        self.modifiers = None
        self.hp = None
        self.mana = None
        self.prot = None
        self.dodge = None
        self.str = None
        self.agi = None
        self.int = None

    def set_modifiers(self, equips):

        modifiers = [GAME_DATA.get(type).get(id).get("modifiers")
                     for type, id in equips.items()
                     if id != ""]

        self.modifiers = modifiers

    def set_stats(self):
        stats = self.stats.copy()
        for item in self.modifiers:
            for index, value in item.items():
                if index == "add":
                    stats = self.add(stats, value)
                if index == "multiply":
                    stats = self.multiply(stats, value)

        self.str = stats.get("str")
        self.agi = stats.get("agi")
        self.int = stats.get("int")
        self.hp = stats.get("hp") + (self.str * 10)
        self.mana = stats.get("mana") + (self.int * 2)
        self.prot = stats.get("prot") + (self.agi // 10)
        self.dodge = stats.get("dodge")
        # self.dodge = stats.get("dodge") + self.agi

    @staticmethod
    def add(base_stat, modifiers):
        for key, value in modifiers.items():
            base_stat[key] += value
        return base_stat

    @staticmethod
    def multiply(base_stat, modifiers):
        for key, value in modifiers.items():
            base_stat[key] *= value
        return base_stat
