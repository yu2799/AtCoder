from sys import stdin
from collections import Counter


def main():
    input = stdin.readline
    _ = int(input())
    a = list(map(int, input().split()))
    print(len(Counter(a).values()))


if __name__ == "__main__":
    main()
