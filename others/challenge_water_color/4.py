from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a = [None] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))

    res = 0
    for i in range(m):
        for j in range(i + 1, m):
            tmp = sum(max(k[i], k[j]) for k in a)
            if res < tmp:
                res = tmp
    print(res)


if __name__ == "__main__":
    main()
