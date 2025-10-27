import unittest


class TestRect(unittest.TestCase):
    def test_rect(self):
        rect = Rect(10, 20)
        self.assertEqual(rect.get_area(), 200)
        self.assertEqual(rect.get_len(), 60)


class Rect:
    def __init__(self, width, height):
        if width > 0 and height > 0:
            self.width = width
            self.height = height
        else:
            print("长和宽必须大于0")
            self.width = 0
            self.height = 0

    def get_area(self):
        return self.width * self.height

    def get_len(self):
        return (self.width + self.height) * 2

    def set_size(self, width: float, height: float):
        self.width = width
        self.height = height


rect = Rect(-10, 20)
# rect.set_size(10, 20)
print(rect.get_area())
print(rect.get_len())
unittest.main()
