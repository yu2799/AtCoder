from sys import stdin


def main():
    input = stdin.readline
    n, d = map(int, input().split())
    s = [list(input()[:-1]) for _ in range(n)]
    res = 0
    cnt = 0
    for i in range(d):
        for j in range(n):
            if s[j][i] == "x":
                cnt = 0
                break
        else:
            cnt += 1
            res = max(res, cnt)
    print(max(res, cnt))


if __name__ == "__main__":
    main()
