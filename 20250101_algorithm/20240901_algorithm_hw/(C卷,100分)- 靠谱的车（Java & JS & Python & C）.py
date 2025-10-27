if __name__ == '__main__':
    while True:
        try:
            dict_novenary = {0: 0, 1: 1, 2: 2, 3: 3, 5: 4, 6: 5, 7: 6, 8: 7, 9: 8}
            N = input().strip()
            num_decimalism = 0
            for i in range(len(N)):
                num_decimalism += dict_novenary[int(N[i])] * (9 ** (len(N) - i - 1))
            print(num_decimalism)
        except:
            break
