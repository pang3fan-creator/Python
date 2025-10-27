card = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
order = range(1, 14)
card_order = dict(zip(card, order))


def dfs(arr, target, temp):
    if len(arr) <= 0:
        return None
    if len(arr) == 1:
        if arr[0] == target:
            return card[arr[0] - 1] + temp
        else:
            return None
    for i in range(len(arr)):
        newArr = arr[:i] + arr[i + 1:]
        first = dfs(newArr, target - arr[i], '+' + card[arr[i] - 1] + temp)
        if first:
            return first
        second = dfs(newArr, target + arr[i], '-' + card[arr[i] - 1] + temp)
        if second:
            return second
        third = dfs(newArr, target * arr[i], '/' + card[arr[i] - 1] + temp)
        if third:
            return third
        fourth = dfs(newArr, target / arr[i], '*' + card[arr[i] - 1] + temp)
        if fourth:
            return fourth


while True:
    try:
        cards = input().split()
        if len(cards) < 4 or 'joker' in cards or 'JOKER' in cards:
            print('ERROR')
        vals = [card_order[x] for x in cards]

        ans = dfs(vals, 24.0, '')

        if ans is not None:
            print(ans)
        else:
            print('NONE')
    except:
        break
