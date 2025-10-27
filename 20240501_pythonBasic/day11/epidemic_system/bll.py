from dtl import EpidemicModel


class EpidemicController:
    def __init__(self):
        self.epidemic_list = []  # type: list[EpidemicModel]

    def add_epidemic(self, epidemic):
        self.epidemic_list.append(epidemic)

    def remove_epidemic(self, name):
        try:
            self.epidemic_list.remove(name)
        except ValueError:
            return False
        else:
            return True

    def update_epidemic(self, name):
        try:
            index_element = self.epidemic_list.index(name)
        except:
            return False
        else:
            return index_element
