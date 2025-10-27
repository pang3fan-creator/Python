if __name__ == '__main__':
    while True:
        try:
            N = int(input())
            dict_country = {}
            for _ in range(N):
                country, gold, silver, bronze = input().strip().split(' ')
                dict_country[country] = [int(gold), int(silver), int(bronze)]
            items_country = sorted(dict_country.items(), key=lambda x: (-x[1][0], -x[1][1], -x[1][2], x[0]))
            list_country = list(map(lambda x: x[0], items_country))
            [print(item) for item in list_country]
        except:
            break
