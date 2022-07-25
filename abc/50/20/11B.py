from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1].lower()
    print(s[0].upper() + s[1:])


if __name__ == "__main__":
    main()
