from sys import stdin


def main():
    input = stdin.readline
    x = int(input())
    res = 0
    a = x // 500
    res += a * 1000
    b = (x - 500 * a) // 5
    res += b * 5
    print(res)


if __name__ == "__main__":
    main()
