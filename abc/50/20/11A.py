from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    print(n % 12 + 1)


if __name__ == "__main__":
    main()
