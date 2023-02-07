from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    res = 0
    for _ in range(n):
        tmp = 0
        for i in range(1, 7):
            tmp += max(res, i)
        res = tmp / 6
    print(res)


if __name__ == "__main__":
    main()
