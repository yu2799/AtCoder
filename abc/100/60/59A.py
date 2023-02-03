from sys import stdin


def main():
    input = stdin.readline
    s = list(map(lambda x: x.upper(), input().split()))
    print(s[0][0] + s[1][0] + s[2][0])


if __name__ == "__main__":
    main()
