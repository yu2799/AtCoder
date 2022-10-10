from collections import deque
from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    q = deque(a)
    res = 0
    while n != 1:
        low = q[0]
        high = q[-1]
        tmp = high % low
        if tmp:
            q.appendleft(tmp)
            q.pop()
        else:
            q.pop()
            n -= 1
        res += 1
    print(res)


if __name__ == "__main__":
    main()
