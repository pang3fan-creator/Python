from dtl import *
from bll import *
from gamelog import GameLog


class GameView:
    """
    游戏视图
    """

    def __init__(self):
        self.choice = "Y"
        self.basic_point = 10
        self.game_log = GameLog()
        self.ctrl = GameController()

    def select_menu(self):
        info = input("请输入对应选项：")
        if info == "1": self.start_game()
        if info == "2": self.print_ranking()
        if info == "3": print(self.game_log.clear_logs())
        if info == "4": exit()

    @staticmethod
    def display_menu():
        print("欢迎参加比牌游戏！澳门赌场欢迎您！！性感荷官在线发牌！")
        print('输入1键开始游戏：\n输入2键查看排名：\n输入3键清空排名：\n输入4键退出游戏：')

    def input_name(self):
        bot_model = BotModel()
        person_model = PersonModel(input("请输入您的名字："))
        self.ctrl.add_player(person_model, bot_model)

    def generate_card(self):
        self.ctrl.list_model[-2].draw_card()
        self.ctrl.list_model[-1].draw_card()

    def display_person_card(self):
        print(self.ctrl.list_model[-2])

    def chose_double(self):
        self.choice = input("本轮是否弃牌？（Y/N）:")
        if self.choice.upper() == "Y":
            self.ctrl.list_model[-2].reduce_point(5)
        else:
            info = input('不加倍(默认)1 /加倍2 /超级加倍3 :')
            if info == '2':
                self.basic_point = 20
            elif info == '3':
                self.basic_point = 30
            else:
                pass

    def compare_card(self):
        if self.choice.upper() != "Y":
            info = self.ctrl.compare_index(self.basic_point)
            print(info)
        self.basic_point = 10
        print(self.ctrl.list_model[-1])

    def append_logs(self):
        self.game_log.add_log(self.ctrl.list_model[-2].record_log())

    def print_ranking(self):
        list_ranking = self.game_log.check_ranking()
        for i in range(len(list_ranking)):
            print(f"第{i + 1}名：{list_ranking[i][1]},比赛轮数：{list_ranking[i][-1]}")

    def start_game(self):
        self.input_name()
        while 100 > self.ctrl.list_model[-2].score > 10:
            self.generate_card()
            self.display_person_card()
            self.chose_double()
            self.compare_card()
        if self.ctrl.list_model[-2].score <= 10:
            print(f"游戏结束，您输了！总共比了{self.ctrl.list_model[-2].count}轮")
        else:
            print(f"游戏结束，您赢了！总共比了{self.ctrl.list_model[-2].count}轮")
            self.append_logs()
