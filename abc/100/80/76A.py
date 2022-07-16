from sys import stdin


def main():
    input = stdin.readline
    r = int(input())
    g = int(input())
    print(g * 2 - r)


if __name__ == "__main__":
    main()
