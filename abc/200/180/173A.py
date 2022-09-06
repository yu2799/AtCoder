from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    print(-n % 1000)


if __name__ == "__main__":
    main()
