from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = [0] + [int(input()) for _ in [0] * n]
    now = 1
    res = 1
    for _ in [0] * n:
        if a[now] == 2:
            print(res)
            exit()
        now = a[now]
        res += 1
    print(-1)


if __name__ == '__main__':
    main()
