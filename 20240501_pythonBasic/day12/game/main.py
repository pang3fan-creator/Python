from usl import GameView

if __name__ == '__main__':
    my_game = GameView()
    while my_game.choice.upper() == "Y":
        my_game.display_menu()
        my_game.select_menu()
        my_game.choice = input("是否继续游戏？Y/N :")
