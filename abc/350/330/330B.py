from sys import stdin


def main():
    input = stdin.readline
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    res = []
    for i in a:
        if i < l:
            res.append(l)
        elif r < i:
            res.append(r)
        else:
            res.append(i)
    print(*res)


if __name__ == "__main__":
    main()
