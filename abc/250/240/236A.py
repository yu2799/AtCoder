from sys import stdin


def main():
    input = stdin.readline
    s = list(input()[:-1])
    a, b = [i - 1 for i in map(int, input().split())]
    s[a], s[b] = s[b], s[a]
    print(*s, sep="")


if __name__ == "__main__":
    main()
