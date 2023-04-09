from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    res = 0
    for i in b:
        res += a[i - 1]
    print(res)


if __name__ == "__main__":
    main()
