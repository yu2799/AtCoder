from sys import stdin


def main():
    input = stdin.readline
    a, b = map(int, input().split())
    print(b if a >= 13 else (b // 2 if a >= 6 else 0))


if __name__ == "__main__":
    main()
