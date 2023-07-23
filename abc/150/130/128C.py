from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    s = [None] * m
    for i in range(m):
        _, *s[i] = map(int, input().split())
    p = list(map(int, input().split()))
    res = 0
    for i in range(2**n):
        for idx, j in enumerate(s):
            cnt = 0
            for k in j:
                if i >> (k - 1) & 1:
                    cnt += 1
            if cnt % 2 != p[idx]:
                break
        else:
            res += 1
    print(res)


if __name__ == "__main__":
    main()
