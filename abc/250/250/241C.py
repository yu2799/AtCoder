from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    s = [list(input()[:-1]) for _ in range(n)]
    for i in range(n):
        cnt = 0
        for j in range(6):
            if s[i][j] == "#":
                cnt += 1
        if cnt >= 4:
            print("Yes")
            return
        for j in range(6, n):
            if s[i][j] == "#":
                cnt += 1
            if s[i][j - 6] == "#":
                cnt -= 1
            if cnt >= 4:
                print("Yes")
                return
    for i in range(n):
        cnt = 0
        for j in range(6):
            if s[j][i] == "#":
                cnt += 1
        if cnt >= 4:
            print("Yes")
            return
        for j in range(6, n):
            if s[j][i] == "#":
                cnt += 1
            if s[j - 6][i] == "#":
                cnt -= 1
            if cnt >= 4:
                print("Yes")
                return
    for i in range(n - 5):
        for j in range(n - 5):
            cnt = 0
            for a in range(6):
                if s[i + a][j + a] == "#":
                    cnt += 1
            if cnt >= 4:
                print("Yes")
                return
    for i in range(n - 5):
        for j in range(5, n):
            cnt = 0
            for a in range(6):
                if s[i + a][j - a] == "#":
                    cnt += 1
            if cnt >= 4:
                print("Yes")
                return

    print("No")


if __name__ == "__main__":
    main()
