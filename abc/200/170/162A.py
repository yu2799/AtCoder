from sys import stdin


def main():
    input = stdin.readline
    n = input()[:-1]
    print("Yes" if n.count("7") else "No")


if __name__ == "__main__":
    main()
