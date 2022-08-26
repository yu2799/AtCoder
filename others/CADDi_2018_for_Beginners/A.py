from sys import stdin


def main():
    input = stdin.readline
    n = input()[:-1]
    print(n.count("2"))


if __name__ == "__main__":
    main()
