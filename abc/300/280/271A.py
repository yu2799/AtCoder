from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    print(format(n, "02X"))


if __name__ == "__main__":
    main()
