def get_result():
    if len(dict_player) == 1:
        print('NULL')
    elif len(dict_player) == 3:
        print('NULL')
    else:
        if 'A' not in dict_player:
            res = sorted(dict_player['B'])
        elif 'B' not in dict_player:
            res = sorted(dict_player['C'])
        else:
            res = sorted(dict_player['A'])
        for item in res:
            print(item)


if __name__ == '__main__':
    dict_player = {}
    while True:
        try:
            player, gesture = input().strip().split(' ')
            dict_player.setdefault(gesture, [])
            dict_player[gesture].append(player)
        except:
            break
    get_result()
