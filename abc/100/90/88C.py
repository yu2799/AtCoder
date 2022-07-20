from sys import stdin


def main():
    input = stdin.readline
    c = [list(map(int, input().split())) for _ in [0] * 3]
    b1 = c[0][0]
    b2 = c[0][1]
    b3 = c[0][2]
    if (c[1][0] - b1 == c[1][1] - b2 == c[1][2] - b3) and (
        c[2][0] - b1 == c[2][1] - b2 == c[2][2] - b3
    ):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
