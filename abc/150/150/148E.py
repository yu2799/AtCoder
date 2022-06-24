from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    if n % 2 != 0:
        print(0)
    else:
        n //= 10
        res = n
        tmp = 5
        while tmp <= n:
            res += n // tmp
            tmp *= 5
        print(res)


if __name__ == "__main__":
    main()
