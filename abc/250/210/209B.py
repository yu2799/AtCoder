from sys import stdin


def main():
    input = stdin.readline
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    print("Yes" if sum(a) - n // 2 <= x else "No")


if __name__ == "__main__":
    main()
