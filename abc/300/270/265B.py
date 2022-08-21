from collections import defaultdict
from sys import stdin


def main():
    input = stdin.readline
    n, m, t = map(int, input().split())
    a = list(map(int, input().split()))
    d = defaultdict(int)
    for _ in [0] * m:
        x, y = map(int, input().split())
        d[x - 2] = y

    for idx, i in enumerate(a):
        t -= i
        if t <= 0:
            print("No")
            return
        t += d[idx]
    print("Yes")


if __name__ == "__main__":
    main()
