from sys import stdin


def meguru_bisect(ng, ok, a, b, x):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if a * mid + b * len(str(mid)) <= x:
            ok = mid
        else:
            ng = mid
    return ok


def main():
    input = stdin.readline
    a, b, x = map(int, input().split())
    ok = 0
    ng = 10**9 + 1
    print(meguru_bisect(ng, ok, a, b, x))


if __name__ == "__main__":
    main()
