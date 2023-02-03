from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    print(n * 800 - n // 15 * 200)


if __name__ == "__main__":
    main()
