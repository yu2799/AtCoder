from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = int(input())
    print("Yes" if n % 500 <= a else "No")


if __name__ == "__main__":
    main()
