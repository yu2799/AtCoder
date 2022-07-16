from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    s = [input()[:-1] for _ in [0] * 2]
    MOD = 10**9 + 7
    cnt = 0
    if s[0][0] == s[1][0]:
        prev = 1
        res = 3
    else:
        prev = 2
        res = 6
    cnt += prev
    while cnt < n:
        if s[0][cnt] == s[1][cnt]:
            if prev == 1:
                res = res * 2 % MOD
            prev = 1
        else:
            if prev == 1:
                res = res * 2 % MOD
            else:
                res = res * 3 % MOD
            prev = 2
        cnt = prev + cnt
    print(res)


if __name__ == "__main__":
    main()
