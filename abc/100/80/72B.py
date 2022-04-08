from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    res = []
    for i in s[::2]:
        res.append(i)
    print(*res, sep="")


if __name__ == "__main__":
    main()
