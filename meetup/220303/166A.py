from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    print("ABC" if s == "ARC" else "ARC")


if __name__ == "__main__":
    main()
