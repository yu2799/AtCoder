from sys import stdin


def main():
    input = stdin.readline
    n, a, b = map(int, input().split())
    s = input()[:-1]
    res = float("inf")
    for i in range(n):
        cnt = 0
        for j in range(n // 2):
            if s[j] != s[n - j - 1]:
                cnt += 1
        tmp = i * a + cnt * b
        if tmp < res:
            res = tmp
        s = s[1:] + s[0]
    print(res)


if __name__ == "__main__":
    main()
