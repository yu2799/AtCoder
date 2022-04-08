from sys import stdin
from math import ceil


def main():
    input = stdin.readline
    x, y = map(int, input().split())
    if x < y:
        print(ceil((y-x) / 10))
    else:
        print(0)


if __name__ == '__main__':
    main()
