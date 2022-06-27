from sys import stdin


def main():
    input = stdin.readline
    n = input()[:-1]
    print((int(n[0]) + int(n[1]) + int(n[2])) * 111)


if __name__ == "__main__":
    main()
