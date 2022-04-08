from sys import stdin


def main():
    input = stdin.readline
    x, y, a, b = map(int, input().split())
    res = 0
    while x < y:
        if x * a < b and x * a < y:
            res += 1
        else:
            break
        x *= a
    res += (y - x - 1) // b
    print(res)


if __name__ == "__main__":
    main()
