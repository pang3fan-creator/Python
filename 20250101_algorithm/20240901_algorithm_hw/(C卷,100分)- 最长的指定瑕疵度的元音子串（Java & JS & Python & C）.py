def main(flaw, s):
    ans, l, r, idxs = 0, 0, 0, []

    for i in range(len(s)):
        if s[i] in yuanSet:  idxs.append(i)

    while r < len(idxs):
        diff = idxs[r] - idxs[l] - (r - l)

        if diff > flaw:
            l += 1
        elif diff < flaw:
            r += 1
        else:
            ans = max(ans, idxs[r] - idxs[l] + 1)
            r += 1

    return ans


if __name__ == '__main__':
    yuanSet = set(list("aeiouAEIOU"))
    print(main(int(input()), input()))
