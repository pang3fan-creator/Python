from typing import List

from dtl import *


class GameController:
    """
    控制类
    """

    def __init__(self):
        self.list_model = []  # type:list[PlayerModel, PersonModel,BotModel]

    def add_player(self, person_model, bot_model):
        self.list_model.append(person_model)
        self.list_model.append(bot_model)

    @staticmethod
    def convert_card(list_card):
        if list_card[0] == list_card[1] == list_card[2]:
            index = list_card[1] * 500
        elif list_card[0] + 1 == list_card[1] == list_card[2] - 1:
            index = list_card[1] * 55
        elif list_card[0] == list_card[1] != list_card[2]:
            index = list_card[1] * 10 + list_card[2]
        elif list_card[0] != list_card[1] == list_card[2]:
            index = list_card[0] + list_card[1] * 10
        else:
            index = list_card[0] / 100 + list_card[1] / 10 + list_card[2]
        return index

    def compare_index(self, basic_point):
        index_person = self.convert_card(self.list_model[-2].hand)
        index_bot = self.convert_card(self.list_model[-1].hand)
        if index_person > index_bot:
            self.list_model[-2].add_point(basic_point)
            self.list_model[-1].reduce_point(basic_point)
            return f"本轮玩家获胜，玩家积分{self.list_model[-2].score}"
        elif index_person < index_bot:
            self.list_model[-2].reduce_point(basic_point)
            self.list_model[-1].add_point(basic_point)
            return f"本轮电脑获胜，玩家积分{self.list_model[-2].score}"
        else:
            self.list_model[-2].add_point(5)
            self.list_model[-1].add_point(5)
            return f"本轮平局，各加5分"
