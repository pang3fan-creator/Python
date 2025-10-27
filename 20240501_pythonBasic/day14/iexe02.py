import iexe01 as ie
from iexe01 import MyClass as MyC
from iexe01 import say_hello, data

if __name__ == '__main__':
    ie.MyClass().say_hi()
    ie.say_hello()
    print(ie.data)

    MyC().say_hi()
    say_hello()
    print(data)
