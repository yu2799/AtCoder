from sys import stdin


def main():
    input = stdin.readline
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    res = 0
    if a[0] < x:
        prev = a[0]
    else:
        res += a[0] - x
        prev = x

    for i in a[1:]:
        if x < i + prev:
            res += i + prev - x
            prev = x - prev
        else:
            prev = i
    print(res)


if __name__ == "__main__":
    main()
