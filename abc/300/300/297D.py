from sys import stdin


def main():
    input = stdin.readline
    a, b = map(int, input().split())
    res = 0
    while b != 0:
        if a > b:
            a, b = b, a
        res += b // a
        b %= a
    print(res - 1)


if __name__ == "__main__":
    main()
