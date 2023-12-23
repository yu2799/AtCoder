from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    res = [a[0]]
    for i in range(1, n):
        tmp = 1 if a[i - 1] < a[i] else -1
        for j in range(a[i - 1] + tmp, a[i], tmp):
            res.append(j)
        res.append(a[i])
    print(*res)


if __name__ == "__main__":
    main()
