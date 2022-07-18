from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    if s[0] == s[1] == s[2]:
        print(-1)
    elif s[0] == s[1]:
        print(s[2])
    elif s[0] == s[2]:
        print(s[1])
    else:
        print(s[0])


if __name__ == "__main__":
    main()
