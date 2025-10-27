# 字符串左移动
def LeftRotateString(ori_str, n):
    # 有效性检查
    if n > len(ori_str):
        rotate_cnt = n % len(ori_str)  # 实际移动数量
    else:
        rotate_cnt = n
    tmp_list = ""
    # 先取出右边剩余的部分
    for i in range(rotate_cnt, len(ori_str)): tmp_list += ori_str[i]
    # 再将左移出的部分添加到右边
    for i in range(0, rotate_cnt): tmp_list += ori_str[i]
    return tmp_list


if __name__ == "__main__":
    test_str = "abcXYZdef"
    new_str = LeftRotateString(test_str, 3)
    print("src:", test_str)
    print("moved:", new_str)
