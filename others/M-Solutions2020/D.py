from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    cur = 1000
    stock = 0

    for i in range(n - 1):
        if a[i] < a[i + 1]:
            stock += cur // a[i]
            cur %= a[i]
        else:
            cur += stock * a[i]
            stock = 0

    print(cur + (stock * a[n - 1] if stock else 0))


if __name__ == "__main__":
    main()
