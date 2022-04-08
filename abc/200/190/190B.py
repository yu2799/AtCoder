from sys import stdin


def main():
    input = stdin.readline
    n, s, d = map(int, input().split())
    for _ in [0] * n:
        x, y = map(int, input().split())
        if x < s and y > d:
            print("Yes")
            exit()
    print("No")


if __name__ == "__main__":
    main()
