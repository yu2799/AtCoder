from sys import stdin


def main():
    input = stdin.readline
    a, b, c, x, y = map(int, input().split())
    res1 = (2*c)*min(x, y) + a*(x-min(x, y)) + b*(y-min(x, y))
    res2 = a*x + b*y
    res3 = 2*c*max(x, y)

    print(min(res1, res2, res3))


if __name__ == '__main__':
    main()
