from math import factorial
from sys import stdin


def main():
    input = stdin.readline
    p = int(input())
    res = 0
    cnt = 10
    while p > 0:
        f = factorial(cnt)
        res += p // f
        p %= f
        cnt -= 1
    print(res)


if __name__ == "__main__":
    main()
