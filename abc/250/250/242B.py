from sys import stdin


def main():
    input = stdin.readline
    s = list(input()[:-1])
    s.sort()
    print(*s, sep="")


if __name__ == "__main__":
    main()
