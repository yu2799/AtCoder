from sys import stdin


def main():
    input = stdin.readline
    n, t = map(int, input().split())
    c = list(map(int, input().split()))
    r = list(map(int, input().split()))
    win = -1
    tmp = 0
    for i in range(n):
        if t == c[i] and tmp < r[i]:
            win = i + 1
            tmp = r[i]
    if win != -1:
        print(win)
        return
    win = 1
    tmp = r[0]
    for i in range(1, n):
        if c[0] == c[i] and tmp < r[i]:
            win = i + 1
            tmp = r[i]
    print(win)


if __name__ == "__main__":
    main()
