from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    res = [0] * n
    for i in range(n):
        for j in range(7):
            res[i] += a[i * 7 + j]
    print(*res)


if __name__ == "__main__":
    main()
