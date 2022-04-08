from sys import stdin


def main():
    input = stdin.readline
    a, b = map(int, input().split())
    if (a == 1 and b == 10) or b - a == 1:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
