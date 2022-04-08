from sys import stdin
from collections import deque


def main():
    input = stdin.readline
    s = input()[:-1]
    q = int(input())
    s = deque(s)
    isReversed = False
    for _ in [0] * q:
        o = input().split()
        if o[0] == "1":
            isReversed = not isReversed
        elif o[1] == "1" and not isReversed or o[1] == "2" and isReversed:
            s.appendleft(o[2])
        else:
            s.append(o[2])

    if isReversed:
        print(*reversed(s), sep="")
    else:
        print(*s, sep="")


if __name__ == '__main__':
    main()
