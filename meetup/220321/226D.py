from sys import stdin
from math import gcd


def main():
    input = stdin.readline
    n = int(input())
    xy = []
    l = []
    for _ in [0] * n:
        x, y = map(int, input().split())
        xy.append((x, y))
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = xy[i]
            x2, y2 = xy[j]
            x = x1 - x2
            y = y1 - y2
            g = gcd(abs(x), abs(y))
            l.append((x // g, y // g))
            l.append((-x // g, -y // g))
    print(len(set(l)))


if __name__ == "__main__":
    main()
