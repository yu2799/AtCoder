from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    b = [list(map(int, input().split())) for _ in range(n)]
    for _ in range(4):
        tmp = [[0] * n for _ in range(n)]
        a = a[::-1]
        for i in range(n):
            for j in range(n):
                tmp[j][n - 1 - i] = a[i][j]
        a = tmp[::-1]
        for i in range(n):
            for j in range(n):
                if a[i][j] and not b[i][j]:
                    break
            else:
                continue
            break
        else:
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    main()
