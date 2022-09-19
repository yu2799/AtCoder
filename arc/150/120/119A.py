from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    res = 10**18
    tmp = 1
    b = 0
    while tmp <= n:
        a = n // tmp
        c = n % tmp
        if a + b + c < res:
            res = a + b + c
        b += 1
        tmp *= 2
    print(res)


if __name__ == "__main__":
    main()
