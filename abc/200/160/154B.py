from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    print("x" * len(s))


if __name__ == "__main__":
    main()
