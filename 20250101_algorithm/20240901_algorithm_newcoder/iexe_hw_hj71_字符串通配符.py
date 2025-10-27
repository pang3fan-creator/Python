import sys


def com(str1, str2):
    if str1 == '' and str2 == '':
        return True
    elif str1 == '' and str2 != '':
        return False
    elif str1 != '' and str2 == '':
        if str1.replace('*', '') == '':
            return True
        else:
            return False
    else:
        if str1[-1] == str2[-1] or (str1[-1] == '?' and str2[-1].isalnum()):
            return com(str1[:-1], str2[:-1])
        elif str1[- 1] == '*':
            return com(str1[:-1], str2) or com(str1, str2[:-1])
        else:
            return False


while True:
    try:
        str1 = input().lower()
        str2 = input().lower()
        if com(str1, str2):
            print('true')
        else:
            print('false')
    except:
        break
