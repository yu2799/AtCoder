from sys import stdin


def main():
    input = stdin.readline
    a, b, c, d = map(int, input().split())
    while True:
        c -= b
        if c <= 0:
            print("Yes")
            return
        a -= d
        if a <= 0:
            print("No")
            return


if __name__ == "__main__":
    main()
