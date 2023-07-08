from collections import defaultdict
from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    c = list(input().split())
    d = list(input().split())
    p = list(map(int, input().split()))
    res = 0
    tmp = defaultdict(int)
    for i in range(m):
        tmp[d[i]] = p[i + 1]
    for i in c:
        if i in tmp:
            res += tmp[i]
        else:
            res += p[0]
    print(res)


if __name__ == "__main__":
    main()
