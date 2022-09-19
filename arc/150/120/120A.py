from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    a = list(map(int, input().split()))
    tmp = 0
    r = 0
    m = a[0]
    res = []
    for idx, i in enumerate(a):
        if m < i:
            m = i
        tmp += i
        r += tmp
        res.append(r + (idx + 1) * m)
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
