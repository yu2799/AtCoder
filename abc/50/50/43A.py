from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    print(n * (n + 1) // 2)


if __name__ == "__main__":
    main()
