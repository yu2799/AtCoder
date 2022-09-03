from collections import deque
from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    q = deque()
    res = 0
    q_sum = 0
    for i in range(m):
        res += (i + 1) * a[i]
        q_sum += a[i]
        q.append(a[i])

    tmp = res
    for i in range(m, n):
        tmp = tmp - q_sum + a[i] * m
        rm = q.popleft()
        q_sum = q_sum - rm + a[i]
        q.append(a[i])
        if res < tmp:
            res = tmp
    print(res)


if __name__ == "__main__":
    main()
