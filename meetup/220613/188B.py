from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    res = 0
    for i, j in zip(a, b):
        res += i * j
    print("No" if res else "Yes")


if __name__ == "__main__":
    main()
