from collections import deque
from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    res = 0
    q = deque()
    q_sum = 0
    for i in range(m):
        res += a[i] * (i + 1)
        q_sum += a[i]
        q.append(a[i])
    tmp = res
    for i in range(m, n):
        tmp = tmp + a[i] * m - q_sum
        q_sum -= q.popleft()
        q_sum += a[i]
        q.append(a[i])
        if res < tmp:
            res = tmp
    print(res)


if __name__ == "__main__":
    main()
