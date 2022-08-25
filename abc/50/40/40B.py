from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    res = float("inf")
    for i in range(int(n**0.5), 0, -1):
        tmp = abs(i - n // i) + n % (i * (n // i))
        if tmp < res:
            res = tmp
    print(res)


if __name__ == "__main__":
    main()
