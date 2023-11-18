from sys import stdin


def main():
    input = stdin.readline
    s = list(input()[:-1])
    print(*s)


if __name__ == "__main__":
    main()
