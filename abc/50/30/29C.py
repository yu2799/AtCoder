from itertools import product
from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    res = ["".join(i) for i in product("abc", repeat=n)]
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
