from math import sqrt
from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    res = set()
    i = 2
    for i in range(2, int(sqrt(n) + 1)):
        tmp = i * i
        while tmp <= n:
            res.add(tmp)
            tmp *= i
    print(n - len(res))


if __name__ == "__main__":
    main()
