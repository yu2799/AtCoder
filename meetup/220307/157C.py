from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    res = [-1] * n
    for _ in [0] * m:
        s, c = map(int, input().split())
        s -= 1
        if res[s] == -1 or res[s] == c:
            res[s] = c
        else:
            print(-1)
            return
    if res[0] == 0 and n != 1:
        print(-1)
        return
    if res[0] == -1 and n != 1:
        res[0] = 1
    for i in range(n):
        if res[i] == -1:
            res[i] = 0
    print(*res, sep="")


if __name__ == "__main__":
    main()
