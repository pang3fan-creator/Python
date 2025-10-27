"""
将一个英文语句以单词为单位逆序排放。例如“I am a boy”，逆序排放后为“boy a am I”
所有单词之间用一个空格隔开，语句中除了英文字母外，不再包含其他字符
输入一个英文语句，每个单词用空格隔开。保证输入只包含空格和字母
I am a boy
boy a am I
nowcoder
nowcoder
"""
import sys

for line in sys.stdin:
    line = line.strip().split(' ')[::-1]
    print(' '.join(line))
