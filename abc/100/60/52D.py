from sys import stdin


def main():
    input = stdin.readline
    n, a, b = map(int, input().split())
    x = list(map(int, input().split()))
    res = 0
    prev = x[0]
    for i in x[1:]:
        tmp = (i - prev) * a
        if tmp < b:
            res += tmp
        else:
            res += b
        prev = i
    print(res)


if __name__ == "__main__":
    main()
