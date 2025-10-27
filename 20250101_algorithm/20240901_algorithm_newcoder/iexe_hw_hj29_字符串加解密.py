while True:
    try:
        a = input()
        b = input()
        m = []
        n = []
        for c in a:
            c = str(c)
            if c == 'Z':
                c = 'a'
            elif c == 'z':
                c = 'A'
            elif c.islower():
                c = chr(ord(c)+1).upper()
            elif c.isupper():
                c = chr(ord(c)+1).lower()
            elif c == '9':
                c = '0'
            elif c.isdigit():
                c = str(int(c) + 1)
            m.append(c)
        print(''.join(m))
        for c in b:
            c = str(c)
            if c == 'a':
                c = 'Z'
            elif c == 'A':
                c = 'z'
            elif c.islower():
                c = chr(ord(c.upper())-1)
            elif c.isupper():
                c = chr(ord(c.lower())-1)
            elif c == '0':
                c = '9'
            elif c.isdigit():
                c = str(int(c) - 1)
            n.append(c)
        print(''.join(n))
    except:
        break