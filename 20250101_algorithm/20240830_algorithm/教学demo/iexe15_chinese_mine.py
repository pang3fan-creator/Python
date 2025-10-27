def num_to_chinese(str_num):
    result, index_max = '', len(str_num) - 1
    if index_max == 0: return num_dict[int(str_num)]
    for i, j in enumerate(str_num):
        temp = index_max - i
        if j != '0': result += (num_dict[int(j)] + pos_dict[10 ** temp])
        if j == '0' and result[-1] != '零': result += '零'

    return result if result[-1] != '零' else result[:-1]


if __name__ == '__main__':
    num_dict = {0: "零", 1: "壹", 2: "贰", 3: "叁", 4: "肆", 5: "伍", 6: "陆", 7: "柒", 8: "捌", 9: "玖", }
    pos_dict = {1: "", 10: "拾", 100: "佰", 1000: "仟", 10000: "万"}
    str_num = str(int(input("请输入一个整数：")))
    print(num_to_chinese(str_num))
