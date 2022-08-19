from sys import stdin


def main():
    input = stdin.readline
    L = int(input())
    print(L * L * L / 27)


if __name__ == "__main__":
    main()
