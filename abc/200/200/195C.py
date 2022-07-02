from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    res = 0
    if n >= 1000:
        res += n - 999
    if n >= 1000000:
        res += n - 999999
    if n >= 1000000000:
        res += n - 999999999
    if n >= 1000000000000:
        res += n - 999999999999
    if n >= 1000000000000000:
        res += n - 999999999999999
    print(res)


if __name__ == "__main__":
    main()
