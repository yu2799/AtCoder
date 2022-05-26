from sys import stdin


def main():
    input = stdin.readline
    a, b, c = map(int, input().split())
    if a == b + c or a + b == c or a + c == b:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
