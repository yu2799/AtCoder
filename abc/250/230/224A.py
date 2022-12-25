from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    print(s[-2:] if s[-2:] == "er" else s[-3:])


if __name__ == "__main__":
    main()
