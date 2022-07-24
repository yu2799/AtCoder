from sys import stdin
from collections import defaultdict


def main():
    input = stdin.readline
    n = int(input())
    d = defaultdict(int)
    s = [input()[:-1] for _ in [0] * n]
    res = []
    for i in s:
        d[i] += 1
        if d[i] >= 2:
            i += f"({d[i] - 1})"
        res.append(i)
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
