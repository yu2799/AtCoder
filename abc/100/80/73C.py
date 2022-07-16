from collections import Counter
from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = Counter([int(input()) for _ in [0] * n])
    print(sum([i % 2 for i in a.values()]))


if __name__ == "__main__":
    main()
