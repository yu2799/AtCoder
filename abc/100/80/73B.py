from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    res = 0
    for _ in [0] * n:
        left, right = map(int, input().split())
        res = res + (right - left) + 1
    print(res)


if __name__ == "__main__":
    main()
