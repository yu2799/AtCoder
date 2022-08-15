from sys import stdin


def main():
    input = stdin.readline
    n, x = map(int, input().split())
    print(x - 1 if x - 1 < n - x else n - x)


if __name__ == "__main__":
    main()
