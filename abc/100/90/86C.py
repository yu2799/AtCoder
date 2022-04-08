from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    nowT, nowX, nowY = 0, 0, 0

    for _ in [0] * n:
        t, x, y = map(int, input().split())
        dt = t - nowT
        d = abs(nowX - x) + abs(nowY - y)
        if dt < d or dt % 2 != d % 2:
            print("No")
            exit()
        nowT, nowX, nowY = t, x, y

    print("Yes")


if __name__ == '__main__':
    main()
