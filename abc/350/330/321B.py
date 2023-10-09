from sys import stdin


def main():
    input = stdin.readline
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if sum(a[:-1]) >= x:
        print(0)
    elif x - sum(a[1:-1]) <= a[-1]:
        print(x - sum(a[1:-1]))
    elif sum(a[1:]) >= x:
        print(a[-1])
    else:
        print(-1)


if __name__ == "__main__":
    main()
