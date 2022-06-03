from sys import stdin


def main():
    input = stdin.readline
    x, y = map(int, input().split())
    print(x + y // 2)


if __name__ == "__main__":
    main()
