from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    print("AC" if s == "Hello,World!" else "WA")


if __name__ == "__main__":
    main()
