from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    t = input()[:-1]
    tmp = ["R G B", "G B R", "B R G"]
    print("Yes" if (s in tmp) == (t in tmp) else "No")


if __name__ == "__main__":
    main()
