from collections import defaultdict
from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    d = defaultdict(int)
    for i in s:
        d[i] += 1
    print("Yes" if len(d.keys()) == 2 and len(set(d.values())) == 1 else "No")


if __name__ == "__main__":
    main()
