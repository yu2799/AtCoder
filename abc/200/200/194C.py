from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = [int(i) for i in input().split()]
    cnt = [0] * 401
    res = 0
    for i in a:
        cnt[i + 200] += 1
    for i in range(401):
        for j in range(i + 1, 401):
            res += cnt[i] * cnt[j] * (i - j) ** 2
    print(res)


if __name__ == "__main__":
    main()
