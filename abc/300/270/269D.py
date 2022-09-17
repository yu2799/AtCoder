from collections import deque
from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    xy = [tuple(map(int, input().split())) for _ in [0] * n]
    res = 0
    flag = [False] * n
    dir = [(0, 1), (1, 1), (1, 0), (0, -1), (-1, -1), (-1, 0)]
    for i in range(n):
        if flag[i]:
            continue
        q = deque()
        q.append(xy[i])
        while q:
            xi, yi = q.pop()
            for x, y in dir:
                for j in range(n):
                    if flag[j]:
                        continue
                    xj, yj = xy[j]
                    if xi + x == xj and yi + y == yj:
                        q.append(xy[j])
                        flag[j] = True
        res += 1
    print(res)


if __name__ == "__main__":
    main()
