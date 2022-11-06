from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    buf = "oxx" * 7
    print("Yes" if s in buf else "No")


if __name__ == "__main__":
    main()
