from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    res = []
    for i in range(k, n):
        if a[i - k] < a[i]:
            res.append("Yes")
        else:
            res.append("No")
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
