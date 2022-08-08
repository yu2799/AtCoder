from sys import stdin


def main():
    input = stdin.readline
    x = int(input())
    print(int(pow(x, 1 / 4)))


if __name__ == "__main__":
    main()
