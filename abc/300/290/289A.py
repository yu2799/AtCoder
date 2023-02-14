from sys import stdin


def main():
    input = stdin.readline
    s = list(input()[:-1])
    for i in range(len(s)):
        if s[i] == "0":
            s[i] = "1"
        else:
            s[i] = "0"
    print(*s, sep="")


if __name__ == "__main__":
    main()
