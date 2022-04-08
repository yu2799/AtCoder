from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    if s[2] == s[3] and s[4] == s[5]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
