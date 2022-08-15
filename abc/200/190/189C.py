from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    for i in range(n):
        tmp = a[i]
        for j in range(i, n):
            if a[j] < tmp:
                tmp = a[j]
            if res < tmp * (j - i + 1):
                res = tmp * (j - i + 1)
    print(res)


if __name__ == "__main__":
    main()
