from sys import stdin


def main():
    input = stdin.readline
    n = input()[:-1]
    print(n[1:], sep="")


if __name__ == "__main__":
    main()
