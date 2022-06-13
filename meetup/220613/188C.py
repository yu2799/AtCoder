from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))

    l = 2 ** (n - 1)

    ml = max(a[:l])
    mr = max(a[l:])

    if ml < mr:
        print(a.index(ml) + 1)
    else:
        print(a.index(mr) + 1)


if __name__ == "__main__":
    main()
