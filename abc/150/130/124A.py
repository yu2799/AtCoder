from sys import stdin


def main():
    input = stdin.readline
    a, b = sorted(map(int, input().split()))
    print(2 * b - 1 if a != b else a + b)


if __name__ == "__main__":
    main()
