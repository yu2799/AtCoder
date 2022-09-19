from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ma = a[0]
    tmp = a[0] * b[0]
    res = [tmp]
    for i in range(1, n):
        if ma < a[i]:
            ma = a[i]
        if tmp < ma * b[i]:
            tmp = ma * b[i]
        res.append(tmp)
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
