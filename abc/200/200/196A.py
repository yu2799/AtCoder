from sys import stdin


def main():
    input = stdin.readline
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max([a - c, a - d, b - c, b - d]))


if __name__ == "__main__":
    main()
