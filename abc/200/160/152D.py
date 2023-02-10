from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    cnt = [[0] * 10 for _ in range(10)]
    for i in range(1, n + 1):
        lower = i % 10
        upper = i // pow(10, len(str(i)) - 1)
        cnt[upper][lower] += 1
    res = 0
    for i in range(10):
        for j in range(10):
            res += cnt[i][j] * cnt[j][i]
    print(res)


if __name__ == "__main__":
    main()
