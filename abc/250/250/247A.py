from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    print("0" + s[:-1])


if __name__ == '__main__':
    main()
