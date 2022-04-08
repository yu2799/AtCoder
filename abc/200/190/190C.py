from sys import stdin
from itertools import product


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    k = int(input())
    cd = [list(map(int, input().split())) for _ in range(k)]

    res = 0
    for choice in product(*cd):
        choice = set(choice)
        tmp = 0
        for a, b in ab:
            if a in choice and b in choice:
                tmp += 1
        if res < tmp:
            res = tmp

    print(res)


if __name__ == '__main__':
    main()
