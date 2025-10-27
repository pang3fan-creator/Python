def num_to_chinese_upcase(num):
    result = ""
    for unit in unit_lst:
        if num <= 0:  break  # 如果数字小于等于0，则退出
        n = num // unit  # 求整数部分

        if len(result) == 0 and n == 0: continue  # 零不作为开头
        if n == 0 and result[-1] == "零":  continue  # 防止出现两个连续零

        upcase = num_dict[n]  # 数字转换成中文大写
        result += upcase  # 中文大写追加到结果后面

        if unit != 1 and n != 0:  # 个位后面面不加单位，0后面不加单位(例如:零仟)
            unit_upcase = num_dict[unit]  # 单位大写
            result += unit_upcase  # 单位大写追加到结果后面
        num = num % unit  # 求余数部分
    return result


if __name__ == '__main__':
    # 数字转换为中文大写
    num_dict = {0: "零", 1: "壹", 2: "贰", 3: "叁", 4: "肆", 5: "伍", 6: "陆",
                7: "柒", 8: "捌", 9: "玖", 10: "拾", 100: "佰", 1000: "仟", 10000: "万"}
    unit_lst = [10000, 1000, 100, 10, 1]

    ch_upcase = num_to_chinese_upcase(int(input("请输入一个数字：")))
    print(ch_upcase)
