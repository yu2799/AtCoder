from sys import stdin


def main():
    input = stdin.readline
    a = int(input())
    b = int(input())
    h = int(input())
    print((a + b) * h // 2)


if __name__ == "__main__":
    main()
