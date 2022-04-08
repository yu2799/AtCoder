from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    res = []
    while n > 0:
        if n % 2 == 0:
            res.append("B")
            n //= 2
        else:
            res.append("A")
            n -= 1
    res.reverse()
    print(*res, sep="")


if __name__ == "__main__":
    main()
