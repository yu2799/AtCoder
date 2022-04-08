from sys import stdin
from typing import OrderedDict


def main():
    input = stdin.readline
    l, r = map(int, input().split())
    s = input()[:-1]
    print(s[:l-1] + s[l-1:r][::-1] + s[r:])


if __name__ == '__main__':
    main()
