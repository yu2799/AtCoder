from collections import deque
from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    res = []
    q = deque(a[:k])
    for i in range(k, n):
        rm = q.popleft()
        res.append("Yes" if rm < a[i] else "No")
        q.append(a[i])
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
