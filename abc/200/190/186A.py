from sys import stdin


def main():
    input = stdin.readline
    n, w = map(int, input().split())
    print(n // w)


if __name__ == "__main__":
    main()
