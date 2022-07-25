from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a = [list(input()[:-1]) for _ in [0] * 2 * n]
    win = [[0, i] for i in range(2 * n)]
    tmp = {
        "G": "C",
        "C": "P",
        "P": "G",
    }
    for i in range(m):
        for j in range(n):
            if tmp[a[win[2 * j][1]][i]] == a[win[2 * j + 1][1]][i]:
                win[2 * j][0] -= 1
            elif tmp[a[win[2 * j + 1][1]][i]] == a[win[2 * j][1]][i]:
                win[2 * j + 1][0] -= 1
        win.sort()
    for _, i in win:
        print(i + 1)


if __name__ == "__main__":
    main()
