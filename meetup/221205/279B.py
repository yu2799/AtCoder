from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    t = input()[:-1]
    print("Yes" if t in s else "No")


if __name__ == "__main__":
    main()
