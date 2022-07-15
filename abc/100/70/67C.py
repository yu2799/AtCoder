from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    a = list(map(int, input().split()))
    left = 0
    right = sum(a)
    res = float("inf")
    for i in a[:-1]:
        left = left + i
        right = right - i
        tmp = abs(left - right)
        if tmp < res:
            res = tmp
    print(res)


if __name__ == "__main__":
    main()
