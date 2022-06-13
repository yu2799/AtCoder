from sys import stdin


def main():
    input = stdin.readline
    x, y = sorted(map(int, input().split()))
    if x + 3 > y:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
