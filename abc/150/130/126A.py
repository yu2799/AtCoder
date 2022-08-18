from sys import stdin


def main():
    input = stdin.readline
    _, k = map(int, input().split())
    s = list(input()[:-1])
    s[k - 1] = s[k - 1].lower()
    print(*s, sep="")


if __name__ == "__main__":
    main()
