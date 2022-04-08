from sys import stdin


def main():
    input = stdin.readline
    p = [int(i) for i in input().split()]
    res = []
    for i in p:
        res.append(chr(96 + i))
    print(*res, sep="")


if __name__ == "__main__":
    main()
