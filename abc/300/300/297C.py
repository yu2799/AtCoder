from sys import stdin


def main():
    input = stdin.readline
    h, w = map(int, input().split())
    s = [list(input()[:-1]) for _ in range(h)]
    for i in range(h):
        for j in range(w - 1):
            if s[i][j] == "T" and s[i][j + 1] == "T":
                s[i][j] = "P"
                s[i][j + 1] = "C"
    for i in s:
        print(*i, sep="")


if __name__ == "__main__":
    main()
