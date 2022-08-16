from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    res = 0
    for i, j in zip(a, b):
        res = res + i * j
    print("Yes" if res == 0 else "No")


if __name__ == "__main__":
    main()
