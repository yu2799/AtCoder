from sys import stdin


def main():
    input = stdin.readline
    n, t = map(int, input().split())
    res = 0
    prev = int(input())
    for _ in [0] * (n - 1):
        a = int(input())
        if a - prev < t:
            res += a - prev
        else:
            res += t
        prev = a
    print(res + t)


if __name__ == "__main__":
    main()
