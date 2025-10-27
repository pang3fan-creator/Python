class EpidemicModel:
    def __init__(self, name, new, now):
        self.name = name
        self.new = new
        self.now = now

    def __str__(self):
        return f"地区名称：{self.name}，新增人数：{self.new}，现有人数：{self.now}"

    def __eq__(self, other):
        return self.name == other
