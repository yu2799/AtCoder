from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    d, x = map(int, input().split())
    res = x
    for _ in [0] * n:
        a = int(input())
        res = res + (d + a - 1) // a
    print(res)


if __name__ == "__main__":
    main()
