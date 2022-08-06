from collections import defaultdict
from sys import stdin


def main():
    input = stdin.readline
    a = map(int, input().split())
    d = defaultdict(int)
    for i in a:
        d[i] += 1
    if len(d.keys()) == 2:
        for i in d.values():
            if i == 2 or i == 3:
                print("Yes")
                return
    print("No")


if __name__ == "__main__":
    main()
