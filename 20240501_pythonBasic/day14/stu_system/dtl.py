class StuModel:
    """
    学生管理模型
    """

    def __init__(self, name='', age=0, score=0):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return f'姓名：{self.name} ，年龄：{self.age} ，分数：{self.score}'

    def __eq__(self, other):
        return self.name == other
