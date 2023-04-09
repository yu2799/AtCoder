from sys import stdin


def main():
    input = stdin.readline
    s = list(input()[:-1])
    for i in range(len(s) // 2):
        s[2 * i], s[2 * i + 1] = s[2 * i + 1], s[2 * i]
    print(*s, sep="")


if __name__ == "__main__":
    main()
