from sys import stdin
from itertools import product


def main():
    input = stdin.readline
    n, _ = map(int, input().split())
    t = [list(map(int, input().split())) for _ in [0] * n]
    for i in product(*t):
        tmp = 0
        for j in i:
            tmp = tmp ^ j
        if tmp == 0:
            print("Found")
            return
    print("Nothing")


if __name__ == "__main__":
    main()
