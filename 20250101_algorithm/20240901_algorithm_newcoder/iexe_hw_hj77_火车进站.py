while True:
    try:
        n = int(input())
        trains = input().strip().split(' ')

        res = []


        def rec_trains(cur_idx, in_trains, out_trains):
            # 如果原始火车列表的最后一个元素已经进站，此时只能出站，将入站列表中的火车倒序加入出站火车中
            if trains[-1] in in_trains:
                res.append(' '.join(out_trains + in_trains[::-1]))
                return
            # 如果进站列表为空，此时只能进站，进站列表加上当前火车，出站列表不变
            elif in_trains == []:
                rec_trains(cur_idx + 1, in_trains + [trains[cur_idx]], out_trains)
            # 否则，就既有可能进站也有可能出站
            else:
                # 出站，当前火车索引不变，进站火车列表减去最后一个元素，出站列表加上进站列表刚刚出站的火车
                rec_trains(cur_idx, in_trains[:-1], out_trains + [in_trains[-1]])
                # 进站，当前火车索引加1，进站列表加上当前火车，出站列表不变
                rec_trains(cur_idx + 1, in_trains + [trains[cur_idx]], out_trains)


        rec_trains(0, [], [])
        res.sort()
        print('\n'.join(res))
    except:
        break
