from sys import stdin


def main():
    input = stdin.readline
    a, p = map(int, input().split())
    print((a * 3 + p) // 2)


if __name__ == "__main__":
    main()