from sys import stdin


def is_ok(n, mid):
    return (mid + 1) * mid // 2 <= n + 1


def main():
    input = stdin.readline
    n = int(input())
    ng = n + 1
    ok = 0
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(n, mid):
            ok = mid
        else:
            ng = mid
    print(n - ok + 1)


if __name__ == "__main__":
    main()
