from sys import stdin
from collections import deque


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    p = [i for i in map(int, input().split())]
    q = deque()
    res = 0
    for i in p[:k]:
        q.append(i)
        res += i
    tmp = res
    for i in p[k:]:
        tmp -= q.popleft()
        q.append(i)
        tmp += i
        if res < tmp:
            res = tmp
    print((res + k) / 2)


if __name__ == "__main__":
    main()
