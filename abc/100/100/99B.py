from sys import stdin


def main():
    input = stdin.readline
    a, b = map(int, input().split())
    d = b - a
    print(d * (d + 1) // 2 - b)


if __name__ == "__main__":
    main()
