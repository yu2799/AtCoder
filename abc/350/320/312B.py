from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    s = (
        [list("." * (m + 2))]
        + [list(".") + list(input()[:-1]) + list(".") for _ in [0] * n]
        + [list("." * (m + 2))]
    )
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (
                i + 2 <= n
                and j + 2 <= m
                and s[i][j] == "#"
                and s[i][j + 1] == "#"
                and s[i + 1][j + 1] == "#"
                and s[i + 1][j] == "#"
                and s[i + 1][j - 1] == "#"
                and s[i][j - 1] == "#"
                and s[i - 1][j - 1] == "#"
                and s[i - 1][j] == "#"
                and s[i - 1][j + 1] == "#"
                and s[i - 1][j + 2] == "."
                and s[i][j + 2] == "."
                and s[i + 1][j + 2] == "."
                and s[i + 2][j - 1] == "."
                and s[i + 2][j] == "."
                and s[i + 2][j + 1] == "."
                and s[i + 2][j + 2] == "."
                and i + 7 <= n
                and j + 7 <= m
                and s[i + 6][j + 6] == "#"
                and s[i + 6][j + 7] == "#"
                and s[i + 7][j + 7] == "#"
                and s[i + 7][j + 6] == "#"
                and s[i + 7][j + 5] == "#"
                and s[i + 6][j + 5] == "#"
                and s[i + 5][j + 5] == "#"
                and s[i + 5][j + 6] == "#"
                and s[i + 5][j + 7] == "#"
                and s[i + 4][j + 4] == "."
                and s[i + 4][j + 5] == "."
                and s[i + 4][j + 6] == "."
                and s[i + 4][j + 7] == "."
                and s[i + 5][j + 4] == "."
                and s[i + 6][j + 4] == "."
                and s[i + 7][j + 4] == "."
            ):
                print(i - 1, j - 1)


if __name__ == "__main__":
    main()
