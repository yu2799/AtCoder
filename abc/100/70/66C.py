from sys import stdin
from collections import deque


def main():
    input = stdin.readline
    n = int(input())
    a = [int(i) for i in input().split()]
    res = deque()
    for i, data in enumerate(a):
        if i % 2:
            res.appendleft(data)
        else:
            res.append(data)
    if n % 2:
        res.reverse()
    print(*res)


if __name__ == "__main__":
    main()
