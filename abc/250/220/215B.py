from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    res = 0
    while pow(2, res + 1) <= n:
        res += 1
    print(res)


if __name__ == "__main__":
    main()
