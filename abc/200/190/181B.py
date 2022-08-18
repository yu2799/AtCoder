from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    res = 0
    for _ in [0] * n:
        a, b = map(int, input().split())
        res += (a + b) * (b - a + 1) // 2
    print(res)


if __name__ == "__main__":
    main()
