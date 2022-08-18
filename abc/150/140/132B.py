from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    p = list(map(int, input().split()))
    res = 0
    for i in range(1, n - 1):
        if p[i - 1] < p[i] < p[i + 1] or p[i + 1] < p[i] < p[i - 1]:
            res += 1
    print(res)


if __name__ == "__main__":
    main()
