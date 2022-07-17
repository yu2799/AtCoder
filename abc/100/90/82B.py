from sys import stdin


def main():
    input = stdin.readline
    s = "".join(sorted(input()[:-1]))
    t = "".join(sorted(input()[:-1], reverse=True))
    print("Yes" if s < t else "No")


if __name__ == "__main__":
    main()
