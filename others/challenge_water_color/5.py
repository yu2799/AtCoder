from sys import stdin


def main():
    input = stdin.readline
    a, b, c, x, y = map(int, input().split())
    res = float("inf")
    for i in range(2 * 10**5 + 1):
        tmp = c * i
        tmp_x = x - i // 2
        tmp_y = y - i // 2
        if 0 < tmp_x:
            tmp += tmp_x * a
        if 0 < tmp_y:
            tmp += tmp_y * b
        if tmp < res:
            res = tmp

    print(res)


if __name__ == "__main__":
    main()
