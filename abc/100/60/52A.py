from sys import stdin


def main():
    input = stdin.readline
    a, b, c, d = map(int, input().split())
    print(a * b if a * b > c * d else c * d)


if __name__ == "__main__":
    main()
