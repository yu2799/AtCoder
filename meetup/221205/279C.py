from collections import defaultdict
from sys import stdin


def main():
    input = stdin.readline
    h, w = map(int, input().split())
    s = [list(input()[:-1]) for _ in [0] * h]
    d1 = defaultdict(int)
    d2 = defaultdict(int)
    for i in range(w):
        buf = ""
        for j in range(h):
            buf += s[j][i]
        d1[buf] += 1
    t = [list(input()[:-1]) for _ in [0] * h]
    for i in range(w):
        buf = ""
        for j in range(h):
            buf += t[j][i]
        d2[buf] += 1
    print("Yes" if d1 == d2 else "No")


if __name__ == "__main__":
    main()
