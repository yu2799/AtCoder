from sys import stdin


def is_ok(a, num, k):
    cnt = 0
    tmp = 0
    prev = 0
    for i in a:
        tmp += i - prev
        if num <= tmp:
            cnt += 1
            tmp = 0
        prev = i
    return cnt < k + 1


def main():
    input = stdin.readline
    _, length = map(int, input().split())
    k = int(input())
    a = list(map(int, input().split())) + [length]
    ng = 0
    ok = a[-1]
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(a, mid, k):
            ok = mid
        else:
            ng = mid
    print(ng)


if __name__ == "__main__":
    main()
