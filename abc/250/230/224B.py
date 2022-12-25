from sys import stdin


def main():
    input = stdin.readline
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in [0] * h]
    for i in range(h - 1):
        for j in range(w - 1):
            if a[i][j] + a[i + 1][j + 1] > a[i + 1][j] + a[i][j + 1]:
                print("No")
                return
    print("Yes")


if __name__ == "__main__":
    main()
