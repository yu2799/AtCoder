from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    py = [tuple(map(int, input().split())) for _ in [0] * m]
    d = {}
    cnt = 1
    prev = 0
    for i, j in sorted(py):
        if prev != i:
            cnt = 1
            d[i] = {}
        d[i][j] = cnt
        cnt += 1
        prev = i
    res = [f"{i:06}{d[i][j]:06}" for i, j in py]
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
