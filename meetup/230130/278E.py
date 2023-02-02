from sys import stdin


def main():
    input = stdin.readline
    H, W, N, h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(H)]
    cnt = [0] * (N + 1)
    for i in range(H):
        for j in range(W):
            cnt[a[i][j]] += 1

    res = [[0] * (W - w + 1) for _ in range(H - h + 1)]
    for i in range(H - h + 1):
        diff_cnt = [0] * (N + 1)
        for a in range(h):
            for b in range(w - 1):
                diff_cnt[a[i + a][b]] += 1

        for j in range(W - w + 1):
            for k in range(i, i + h):
                diff_cnt[a[k][j + w]] += 1

            tmp = 0
            for k in range(N + 1):
                if cnt[k] - diff_cnt[k] > 0:
                    tmp += 1
            res[i][j] = tmp

            for k in range(i, i + h):
                diff_cnt[a[k][j]] -= 1

    for row in res:
        print(*row)


if __name__ == "__main__":
    main()
