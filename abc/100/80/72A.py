from sys import stdin


def main():
    input = stdin.readline
    x, t = map(int, input().split())
    print(x - t if x - t > 0 else 0)


if __name__ == "__main__":
    main()
