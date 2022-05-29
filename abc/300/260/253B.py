from sys import stdin


def main():
    input = stdin.readline
    h, w = map(int, input().split())
    s = [input()[:-1] for _ in [0] * h]
    flag = False
    x = [0, 0]
    y = [0, 0]
    for i in range(h):
        for j in range(w):
            if flag and s[i][j] == "o":
                y = [i, j]
                print(abs(y[0] - x[0] + abs(y[1] - x[1])))
                return
            if s[i][j] == "o":
                x = [i, j]
                flag = True


if __name__ == "__main__":
    main()
