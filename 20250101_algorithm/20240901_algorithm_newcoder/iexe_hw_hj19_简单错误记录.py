err_list = []
cnt_list = []

while True:
    try:
        s = input().split(' ')
        f = s[0].split('\\')[-1]
        item = f'{f[-16:]} {s[1]}'
        try:
            i = err_list.index(item)
            cnt_list[i] += 1
        except ValueError:
            err_list.append(item)
            cnt_list.append(1)
    except Exception:
        break

for i in range((len(err_list) - 8) if len(err_list) > 8 else 0, len(err_list)):
    print(err_list[i], cnt_list[i])
