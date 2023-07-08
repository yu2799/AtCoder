from collections import defaultdict
from operator import itemgetter
from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(int)
    tmp = {i + 1: 0 for i in range(n)}
    for i in range(len(a)):
        d[a[i]] += 1
        if d[a[i]] == 2:
            tmp[a[i]] = i + 1
    res = sorted(tmp.items(), key=itemgetter(1))
    for i, _ in res:
        print(i, end=" ")


if __name__ == "__main__":
    main()
