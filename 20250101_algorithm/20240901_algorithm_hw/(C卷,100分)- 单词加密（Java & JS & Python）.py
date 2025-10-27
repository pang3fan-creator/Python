if __name__ == '__main__':
    while True:
        try:
            set_vowel = {'a', 'e', 'o', 'u', 'i', 'A', 'E', 'O', 'U', 'I'}
            list_words = input().strip().split(' ')
            for i, words in enumerate(list_words):
                judge = True
                for item in words:
                    if item in set_vowel:
                        list_words[i] = list_words[i].replace(item, '*')
                        judge = False
                if judge:
                    list_words[i] = list_words[i][-1] + list_words[i][1:-1] + list_words[i][0]
            print(' '.join(list_words))
        except:
            break
