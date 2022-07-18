from sys import stdin
from math import ceil


def main():
    input = stdin.readline
    _ = int(input())
    a = list(map(int, input().split()))
    tmp = [i for i in a if i > 0]
    print(ceil(sum(tmp) / len(tmp)))


if __name__ == "__main__":
    main()
