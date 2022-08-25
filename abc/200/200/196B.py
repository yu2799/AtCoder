from sys import stdin


def main():
    input = stdin.readline
    x = input()[:-1].split(".")
    print(x[0])


if __name__ == "__main__":
    main()
