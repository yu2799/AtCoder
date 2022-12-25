from sys import stdin


def main():
    input = stdin.readline
    a, b, c, d = map(int, input().split())
    tmp = c * d - b
    print((a + tmp - 1) // tmp if 0 < tmp else -1)


if __name__ == "__main__":
    main()
