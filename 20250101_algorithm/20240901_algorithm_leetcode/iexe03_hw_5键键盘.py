"""
【5键键盘的输出】有一个特殊的 5键键盘，上面有 a,ctrl-c,ctrl-x,ctrl-v,ctrl-a五个键。
a键在屏幕上输出一个字母 a;
ctrl-c将当前选择的字母复制到剪贴板;
ctrl-x将当前选择的 字母复制到剪贴板，并清空选择的字母;
ctrl-v将当前剪贴板里的字母输出到屏幕;
ctrl-a 选择当前屏幕上所有字母。
注意:
1、剪贴板初始为空，新的内容被复制到剪贴板时会覆盖原来的内容
2、当屏幕上没有字母时，ctrl-a无效
3、当没有选择字母时，ctrl-c和 ctrl-x无效
4、当有字母被选择时，a和ctrl-v这两个有输出功能的键会先清空选择的字母，再进行输出
给定一系列键盘输入，输出最终屏幕上字母的数量。
输入描述:
输入为一行，为简化解析，用数字 12345代表 a,ctrl-c,ctrl-x,ctrl-v,ctrl-a五个键的输入，数字用空格分隔
输出描述:
输出一个数字，为最终屏目上字母的数量。
示例:
输入
111
输出
3
"""


def get_result():
    cou, sel, clip = 0, 0, 0

    for v in str_input:
        if v == '5': sel = cou
        if v == '2': clip, sel = sel, 0
        if v == '1': cou, sel = cou - sel + 1, 0
        if v == '3': clip, cou, sel = sel, cou - sel, 0
        if v == '4': cou, sel, clip = cou - sel + clip, 0, 0

    return cou


if __name__ == '__main__':
    str_input = input()
    print(get_result())
