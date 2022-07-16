from sys import stdin


def main():
    input = stdin.readline
    x, y, z = map(int, input().split())
    print((x - z) // (y + z))


if __name__ == "__main__":
    main()
