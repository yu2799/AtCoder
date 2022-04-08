from sys import stdin


def main():
    input = stdin.readline
    n, q = map(int, input().split())
    a = [int(i) for i in input().split()]
    res = []
    shift = 0
    for _ in [0] * q:
        t, x, y = map(int, input().split())
        x = x - 1 - shift
        y = y - 1 - shift
        if t == 1:
            a[x], a[y] = a[y], a[x]
        elif t == 2:
            shift = (shift + 1) % n
        else:
            res.append(a[x])
    print(*res, sep="\n")


if __name__ == '__main__':
    main()
