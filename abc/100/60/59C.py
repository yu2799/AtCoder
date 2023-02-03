from sys import stdin


def solve(a, diff):
    res = 0
    tmp = 0
    for i in range(len(a)):
        tmp += a[i]
        if diff:
            if tmp <= 0:
                res += 1 - tmp
                tmp = 1
        else:
            if tmp >= 0:
                res += 1 + tmp
                tmp = -1
        diff = not diff
    return res


def main():
    input = stdin.readline
    _ = int(input())
    a = list(map(int, input().split()))
    print(min(solve(a, True), solve(a, False)))


if __name__ == "__main__":
    main()
