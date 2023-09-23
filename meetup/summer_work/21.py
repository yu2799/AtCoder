from sys import stdin


def main():
    input = stdin.readline
    n, q = map(int, input().split())
    res = list(range(1, n + 1))
    tmp = list(range(-1, n))
    for _ in range(q):
        x = int(input())
        i = tmp[x]
        if i < n - 1:
            j = i + 1
        else:
            j = i - 1
        y = res[j]
        res[i] = y
        res[j] = x
        tmp[x] = j
        tmp[y] = i
    print(*res)


if __name__ == "__main__":
    main()
