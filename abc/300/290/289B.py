from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    i = 0
    tmp = []
    res = []
    for i in range(1, n + 1):
        tmp.append(i)
        if i not in a:
            while tmp:
                res.append(tmp.pop())

    while tmp:
        res.append(tmp.pop())
    print(*res)


if __name__ == "__main__":
    main()
