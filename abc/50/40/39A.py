from sys import stdin


def main():
    input = stdin.readline
    a, b, c = map(int, input().split())
    print((a * b + b * c + a * c) * 2)


if __name__ == "__main__":
    main()
