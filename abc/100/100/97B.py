from sys import stdin
from math import sqrt


def main():
    input = stdin.readline
    x = int(input())
    r = int(sqrt(x))
    res = 1
    for b in range(1, r + 1):
        for p in range(2, r + 1):
            tmp = b**p
            if tmp <= x and res < tmp:
                res = tmp
    print(res)


if __name__ == "__main__":
    main()
