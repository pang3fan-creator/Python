if __name__ == '__main__':
    while True:
        try:
            list_str = input().strip().split(',')
            list_str = sorted(list_str, key=lambda x: (x[0:2], -int(x[2:])))
            print(','.join(list_str))
        except:
            break
