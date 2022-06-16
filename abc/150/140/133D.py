from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    res = [0] * n
    for i in range(n):
        if i % 2 == 0:
            res[0] += a[i]
        else:
            res[0] -= a[i]
    for i in range(1, n):
        res[i] = 2 * a[i - 1] - res[i - 1]
    print(*res)


if __name__ == "__main__":
    main()
