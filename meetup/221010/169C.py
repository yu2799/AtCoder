from sys import stdin


def main():
    input = stdin.readline
    a, b = input().split()
    a = int(a)
    b, c = map(int, b.split("."))
    print(a * (b * 100 + c) // 100)


if __name__ == "__main__":
    main()
