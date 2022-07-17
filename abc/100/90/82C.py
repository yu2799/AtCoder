from sys import stdin
from collections import defaultdict


def main():
    input = stdin.readline
    _ = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(int)
    for i in a:
        d[i] += 1
    print(
        sum(
            [
                value - key if key <= value else value
                for key, value in d.items()
            ]
        )
    )


if __name__ == "__main__":
    main()
