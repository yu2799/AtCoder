from collections import defaultdict
from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    s = input()[:-1]
    d = defaultdict(int)
    prev = s[0]
    cnt = 1
    for i in s[1:]:
        if prev == i:
            cnt += 1
        else:
            d[prev] = max(cnt, d[prev])
            cnt = 1
            prev = i
    d[prev] = max(cnt, d[prev])

    res = 0
    for i in d.values():
        res += i
    print(res)


if __name__ == "__main__":
    main()
