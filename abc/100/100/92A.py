from sys import stdin


def main():
    input = stdin.readline
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    print(min(a, b) + min(c, d))


if __name__ == "__main__":
    main()
