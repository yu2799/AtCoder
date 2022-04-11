from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    print(f"{s[0]}{len(s) - 2}{s[-1]}")


if __name__ == '__main__':
    main()
