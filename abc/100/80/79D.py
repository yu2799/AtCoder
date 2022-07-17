from sys import stdin


def main():
    input = stdin.readline
    h, w = map(int, input().split())
    c = [list(map(int, input().split())) for _ in [0] * 10]
    res = 0
    for k in range(10):
        for i in range(10):
            for j in range(10):
                c[i][j] = min(c[i][j], c[i][k] + c[k][j])
    a = [list(map(int, input().split())) for _ in [0] * h]
    for y in range(h):
        for x in range(w):
            if a[y][x] >= 0:
                res = res + c[a[y][x]][1]
    print(res)


if __name__ == "__main__":
    main()
