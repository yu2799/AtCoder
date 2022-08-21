from sys import stdin


def main():
    input = stdin.readline
    a, b = map(int, input().split())
    print(100 * (1 - b / a))


if __name__ == "__main__":
    main()
