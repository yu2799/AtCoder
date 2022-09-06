from sys import stdin


def main():
    input = stdin.readline
    x, y, z = map(int, input().split())
    print((y * z - 1) // x)


if __name__ == "__main__":
    main()
