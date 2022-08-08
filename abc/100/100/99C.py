from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    res = n
    for i in range(n + 1):
        d = 0
        t = i
        while t > 0:
            d += t % 6
            t //= 6
        t = n - i
        while t > 0:
            d += t % 9
            t //= 9
        if d < res:
            res = d
    print(res)


if __name__ == "__main__":
    main()
