from sys import stdin


def main():
    input = stdin.readline
    a = [[int(i) for i in input().split()] for _ in [0] * 3]
    n = int(input())
    bingo = [[False] * 3 for _ in [0] * 3]
    for _ in [0] * n:
        b = int(input())
        for i in range(3):
            for j in range(3):
                if a[i][j] == b:
                    bingo[i][j] = True
    for i in range(3):
        if bingo[i][0] and bingo[i][1] and bingo[i][2]:
            print("Yes")
            return
        if bingo[0][i] and bingo[1][i] and bingo[2][i]:
            print("Yes")
            return
    else:
        if bingo[0][0] and bingo[1][1] and bingo[2][2]:
            print("Yes")
        elif bingo[0][2] and bingo[1][1] and bingo[2][0]:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
