from sys import stdin


def main():
    input = stdin.readline
    a = input()[:-1]
    b = input()[:-1]
    print(a if len(a) > len(b) else b)


if __name__ == "__main__":
    main()
