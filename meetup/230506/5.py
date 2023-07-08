from sys import stdin


def main():
    input = stdin.readline
    h, w = map(int, input().split())
    s = [list(input()[:-1]) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if s[i][j] == ".":
                continue

            if i - 1 >= 0 and s[i - 1][j] == "#":
                continue
            if i + 1 < h and s[i + 1][j] == "#":
                continue
            if j - 1 >= 0 and s[i][j - 1] == "#":
                continue
            if j + 1 < w and s[i][j + 1] == "#":
                continue
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    main()
