import random


class PlayerModel:
    """
    父类
    """

    def __init__(self):
        self.name = ''
        self.hand = []
        self.score = 50
        self.count = 0

    def draw_card(self):
        self.hand = random.sample(
            [i for i in range(1, 11)] * 4, 3)
        self.hand.sort()

    def add_point(self, index):
        self.score += index
        self.count += 1

    def reduce_point(self, index):
        self.score -= index
        self.count += 1

    def record_log(self):
        return f"玩家名字,{self.name},最终分数,{self.score},比牌次数,{self.count}"


class PersonModel(PlayerModel):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return f'\n玩家：{self.name}，手牌{self.hand}，积分：{self.score}'


class BotModel(PlayerModel):
    def __init__(self):
        super().__init__()
        self.name = 'bot'
        self.score = 10000

    def __str__(self):
        return f'机器人手牌{self.hand}'
