def make_set(list_1):
    return {(int(list_1[i]), int(list_1[i + 1])) for i in range(0, len(list_1), 2)}


def main(set_1, set_union):
    list_offset = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    set_new = set()
    for item in set_1:
        for offset in list_offset:
            x_new, y_new = item[0] + offset[0], item[1] + offset[1]

            if 0 <= x_new <= 18 and 0 <= y_new <= 18 and (x_new, y_new) not in set_union:
                set_new.add((x_new, y_new))

    return len(set_new)


if __name__ == '__main__':
    s_white = make_set(list(map(int, input().split())))
    s_black = make_set(list(map(int, input().split())))
    s_union = s_white | s_black

    print(f"{main(s_white, s_union)} {main(s_black, s_union)}")
