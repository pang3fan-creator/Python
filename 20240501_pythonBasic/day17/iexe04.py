"""
需求：在旧的功能上添加新功能，同时不能破坏旧的功能
"""


def old_func():
    print("old_func")

    def new_func():
        print("new_func")


old_func()
