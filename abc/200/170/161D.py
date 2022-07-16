from sys import stdin
from collections import deque


def main():
    input = stdin.readline
    k = int(input())
    q = deque([i for i in range(1, 10)])
    for _ in [0] * k:
        rm = q.popleft()
        tmp = rm % 10
        if tmp != 0:
            q.append(10 * rm + tmp - 1)
        q.append(10 * rm + tmp)
        if tmp != 9:
            q.append(10 * rm + tmp + 1)
    print(rm)


if __name__ == "__main__":
    main()
