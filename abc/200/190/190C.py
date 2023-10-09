from itertools import product
from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(m)]
    k = int(input())
    cd = [tuple(map(int, input().split())) for _ in range(k)]
    res = 0
    for i in product(*cd):
        tmp = set(i)
        cnt = 0
        for a, b in ab:
            if a in tmp and b in tmp:
                cnt += 1
        if res < cnt:
            res = cnt
    print(res)


if __name__ == "__main__":
    main()
