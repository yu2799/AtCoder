from sys import stdin
from collections import deque


def main():
    input = stdin.readline
    n = int(input())
    a = [int(i) for i in input().split()]
    cake = sum(a)
    if cake % 10 != 0:
        print("No")
    else:
        cake //= 10
        q = deque()
        now = 0
        a += a
        for i in a:
            q.append(i)
            now += i
            while q and cake < now:
                rm = q.popleft()
                now -= rm
            if cake == now:
                print("Yes")
                exit()
        else:
            print("No")


if __name__ == '__main__':
    main()
