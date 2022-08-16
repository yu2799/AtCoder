from sys import stdin


def main():
    input = stdin.readline
    a, b, c = map(int, input().split())
    print(c // a if a < b else c // b)


if __name__ == "__main__":
    main()
