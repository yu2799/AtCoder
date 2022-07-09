from sys import stdin


def main():
    input = stdin.readline
    n, r = map(int, input().split())
    print(r if n >= 10 else r + 100 * (10 - n))


if __name__ == "__main__":
    main()
