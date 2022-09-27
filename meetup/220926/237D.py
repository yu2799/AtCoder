from collections import deque
from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    s = input()[:-1]
    res = deque([n])
    for idx, i in enumerate(reversed(s)):
        if i == "L":
            res.append(n - idx - 1)
        else:
            res.appendleft(n - idx - 1)
    print(*res)


if __name__ == "__main__":
    main()
