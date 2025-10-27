while 1:
    try:
        a = input()
        b = a.split('.')
        if len(b) != 4:
            print('NO')
        else:
            if 0 <= int(b[0]) < 256 and 0 <= int(b[1]) < 256 and 0 <= int(b[2]) < 256 and 0 <= int(b[3]) < 256:
                print('YES')
            else:
                print('NO')
    except:
        break
