from collections import defaultdict
from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    d = defaultdict(int)
    for i in a:
        d[i] += 1
    tmp = list(sorted(d))
    res = 0
    for i in range(min(k, len(tmp))):
        if i != tmp[i]:
            print(i)
            return
        res += 1
    print(res)


if __name__ == "__main__":
    main()
