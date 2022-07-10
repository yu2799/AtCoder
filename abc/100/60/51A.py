from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    print(*s.split(","))


if __name__ == "__main__":
    main()
