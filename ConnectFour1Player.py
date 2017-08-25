import ConnectFourRandomAI
import ConnectFourMinimaxAI
import ConnectFourMinimaxWithABPruningAI2

import ConnectFourEngine

if __name__ == '__main__':
    # Initialise the game engine
    # Modify these parameters to tweak the game
    app = ConnectFourEngine.ConnectFour(
            ai_delay = 20,
            red_player = None,
            blue_player = ConnectFourMinimaxWithABPruningAI2.AIcheck,
            )
    # start the game engine
    app.game_loop()
