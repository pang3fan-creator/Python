if __name__ == '__main__':
    while True:
        try:
            str_l = input().strip()
            k = int(input())
            str_new = ''
            for i in range(len(str_l) - 1): str_new += str_l[i] if str_l[i] == str_l[i + 1] else str_l[i] + ','
            str_new += str_l[-1]
            str_new = str_new.split(',')
            dict_letter = {}
            for item in str_new:
                dict_letter.setdefault(item[0], 0)
                dict_letter[item[0]] = max(dict_letter[item[0]], len(item))
            items_letter = sorted(dict_letter.items(), key=lambda x: (-x[1], x[0]))
        except:
            break
