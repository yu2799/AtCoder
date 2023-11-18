from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    f = [0] * n
    s = [0] * n
    tmp = 0
    select = -1
    for i in range(n):
        f[i], s[i] = map(int, input().split())
        if tmp < s[i]:
            tmp = s[i]
            select = i
    res = 0
    for i in range(n):
        if i == select:
            continue
        res = max(res, tmp + s[i] // (2 if f[i] == f[select] else 1))
    print(res)


if __name__ == "__main__":
    main()
