from sys import stdin


def main():
    input = stdin.readline
    x1, y1, x2, y2 = map(int, input().split())
    dx = x2 - x1
    dy = y2 - y1

    x3 = -dy + x2
    y3 = dx + y2

    dx = x3 - x2
    dy = y3 - y2

    x4 = -dy + x3
    y4 = dx + y3
    print(x3, y3, x4, y4)


if __name__ == "__main__":
    main()
