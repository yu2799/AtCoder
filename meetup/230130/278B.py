from sys import stdin


def convert(h, m):
    h1 = h // 10
    h2 = h % 10
    m1 = m // 10
    m2 = m % 10
    nh = h1 * 10 + m1
    nm = h2 * 10 + m2
    return nh, nm


def check(h, m):
    return 0 <= h <= 23 and 0 <= m <= 59


def next(h, m):
    if m + 1 == 60:
        h += 1
    return h % 24, (m + 1) % 60


def main():
    input = stdin.readline
    h, m = map(int, input().split())
    while not check(*convert(h, m)):
        h, m = next(h, m)
    print(h, m)


if __name__ == "__main__":
    main()
