from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    print(((n + 1) // 2) / n)


if __name__ == "__main__":
    main()
