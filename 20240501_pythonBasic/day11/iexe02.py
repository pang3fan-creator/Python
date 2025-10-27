class Owner:
    def __init__(self, own_name, clean_name=''):
        self.name = own_name
        self.cleaner = Cleaner(clean_name)

    def clean_room(self):
        print(f"{self.name}叫{self.cleaner}去打扫房间")


class Cleaner:
    def __init__(self, name=''):
        self.name = name

    def __str__(self):
        return f"{self.name}阿姨"


owner_lihua = Owner('李华', '小红')
owner_lihua.clean_room()
