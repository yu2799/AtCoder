from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    t = input()[:-2]
    print("Yes" if s == t else "No")


if __name__ == "__main__":
    main()
