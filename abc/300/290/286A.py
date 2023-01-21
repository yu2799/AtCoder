from sys import stdin


def main():
    input = stdin.readline
    n, p, q, r, s = map(lambda x: int(x) - 1, input().split())
    a = list(map(int, input().split()))
    for i in range(q - p + 1):
        tmp = a[i + p]
        a[i + p] = a[i + r]
        a[i + r] = tmp
    print(*a)


if __name__ == "__main__":
    main()
