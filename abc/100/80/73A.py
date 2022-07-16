from sys import stdin


def main():
    input = stdin.readline
    n = list(input()[:-1])
    print("Yes" if "9" in n else "No")


if __name__ == "__main__":
    main()
