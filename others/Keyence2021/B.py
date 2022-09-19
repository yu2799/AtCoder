from collections import Counter
from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    a = Counter(map(int, input().split()))
    res = 0
    for i in range(n):
        if a[i] < k:
            res += i * (k - a[i])
            k = a[i]
        if k == 0:
            break
    print(res)


if __name__ == "__main__":
    main()
