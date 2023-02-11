from bisect import bisect_left
from sys import stdin


def main():
    input = stdin.readline
    h, w = map(int, input().split())
    s = [list(input()[:-1]) for _ in range(h)]
    tmp_h = []
    tmp_w = []
    for i in range(h):
        tmp_h.append([-1] + [j for j in range(w) if s[i][j] == "#"] + [w])
    for i in range(w):
        tmp_w.append([-1] + [j for j in range(h) if s[j][i] == "#"] + [h])

    res = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                continue
            idx_i = bisect_left(tmp_w[j], i)
            idx_j = bisect_left(tmp_h[i], j)
            tmp = (
                tmp_h[i][idx_j]
                - tmp_h[i][idx_j - 1]
                + tmp_w[j][idx_i]
                - tmp_w[j][idx_i - 1]
            ) - 3
            if res < tmp:
                res = tmp
    print(res)


if __name__ == "__main__":
    main()
