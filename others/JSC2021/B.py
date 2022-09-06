from collections import defaultdict
from sys import stdin


def main():
    input = stdin.readline
    _ = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    tmp = defaultdict(int)
    for i in a:
        tmp[i] += 1
    for i in b:
        tmp[i] += 1
    res = [i for i, j in tmp.items() if j == 1]
    res.sort()
    print(*res)


if __name__ == "__main__":
    main()
