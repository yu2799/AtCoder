from itertools import product
from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    res = 0
    for i in range(3, len(str(n)) + 1):
        for j in product("357", repeat=i):
            tmp = "".join(j)
            if "3" in tmp and "5" in tmp and "7" in tmp and int(tmp) <= n:
                res += 1
    print(res)


if __name__ == "__main__":
    main()
