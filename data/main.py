from data.control import Control
from data.states import Game, Splash, GameOver
from data.load import Player


def main():

    app = Control()
    state_dict = {
        "GAME": Game(),
        "SPLASH": Splash(),
        "GAMEOVER": GameOver()
    }
    app.state_machine.setup(state_dict, "SPLASH")
    app.state_machine.state.persistent = Player
    app.run()
