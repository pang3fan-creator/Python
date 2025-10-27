import pickle
from usl import GameView
from dtl import PlayerModel, PersonModel, BotModel
from bll import GameController

with open("save_game.pkl", "wb") as file:
    pickle.dump((GameView, PlayerModel, PersonModel, BotModel, GameController), file)

with open("save_game.pkl", "rb") as file:
    GameView, PlayerModel, PersonModel, BotModel, GameController = pickle.load(file)

if __name__ == '__main__':
    my_game = GameView()
    while my_game.choice.upper() == "Y":
        my_game.main_menu()
        my_game.__select_menu()
        my_game.choice = input("是否继续游戏？Y/N :")
