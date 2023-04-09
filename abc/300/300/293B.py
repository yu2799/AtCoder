from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    tmp = [False] * n
    for i in range(n):
        if not tmp[i]:
            tmp[a[i] - 1] = True
    k = 0
    res = []
    for i in range(n):
        if not tmp[i]:
            res.append(i + 1)
            k += 1
    print(k)
    print(*res)


if __name__ == "__main__":
    main()
