from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    res = []
    for i in range(1, int(pow(n, 0.5)) + 1):
        if n % i == 0:
            res.append(i)
            if i ** 2 != n:
                res.append(n // i)
    res.sort()
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
