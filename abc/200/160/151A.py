from sys import stdin


def main():
    input = stdin.readline
    c = input()[:-1]
    print(chr(ord(c) + 1))


if __name__ == "__main__":
    main()
