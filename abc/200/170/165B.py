from sys import stdin


def main():
    input = stdin.readline
    x = int(input())
    tmp = 100
    res = 0
    while True:
        tmp *= 101
        tmp //= 100
        res += 1
        if x <= tmp:
            print(res)
            return


if __name__ == "__main__":
    main()
