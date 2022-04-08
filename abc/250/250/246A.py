from sys import stdin


def main():
    input = stdin.readline
    p = [list(map(int, input().split())) for _ in [0] * 3]
    x = p[0][0]
    y = p[0][1]
    if x == p[1][0]:
        x = p[2][0]
    elif x == p[2][0]:
        x = p[1][0]

    if y == p[1][1]:
        y = p[2][1]
    elif y == p[2][1]:
        y = p[1][1]
    print(x, y)


if __name__ == "__main__":
    main()
