from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    res = 10**9 + 1
    for _ in [0] * n:
        a, p, x = map(int, input().split())
        if a < x and p < res:
            res = p
    print(res if res != 10**9 + 1 else -1)


if __name__ == "__main__":
    main()
