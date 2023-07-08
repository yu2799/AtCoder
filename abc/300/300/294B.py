from sys import stdin


def main():
    input = stdin.readline
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    res = [""] * h
    for i in range(h):
        for j in range(w):
            if a[i][j] == 0:
                res[i] += "."
            else:
                res[i] += chr(64 + a[i][j])
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
