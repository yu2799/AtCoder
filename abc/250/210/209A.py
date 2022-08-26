from sys import stdin


def main():
    input = stdin.readline
    a, b = map(int, input().split())
    print(max(b - a + 1, 0))


if __name__ == "__main__":
    main()
