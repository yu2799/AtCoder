from sys import stdin


def main():
    input = stdin.readline
    w, h, n = map(int, input().split())
    res = [[0, w], [0, h]]
    for _ in [0] * n:
        x, y, a = map(int, input().split())
        if a == 1 and res[0][0] < x:
            res[0][0] = x
        if a == 2 and res[0][1] > x:
            res[0][1] = x
        if a == 3 and res[1][0] < y:
            res[1][0] = y
        if a == 4 and res[1][1] > y:
            res[1][1] = y
    if res[0][0] < res[0][1] and res[1][0] < res[1][1]:
        print((res[0][1] - res[0][0]) * (res[1][1] - res[1][0]))
    else:
        print(0)


if __name__ == "__main__":
    main()
