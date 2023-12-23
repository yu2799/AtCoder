from collections import defaultdict
from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    d = defaultdict(int)
    for i in a:
        d[i] += 1
    for i in b:
        d[i] -= 1
        if d[i] < 0:
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    main()
