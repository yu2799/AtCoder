from sys import stdin


def is_ok(m, a, k):
    cnt = 0
    tmp = 0

    for i in a:
        tmp += i
        if tmp >= m:
            cnt += 1
            tmp = 0
        print(tmp)
    print(cnt)
    return cnt >= k + 1


def main():
    input = stdin.readline
    n, l = map(int, input().split())
    k = int(input())
    a = [0] + [int(i) for i in input().split()] + [l]
    left = 0
    right = l // (k + 1) + 1   # k+1個に分割する = 全体の長さを最大化するには l // k 以下である必要がある
    while right - left > 1:
        m = (left + right) // 2
        # print(left, right, m)
        if is_ok(m, a, k):
            left = m
        else:
            right = m

    print(left)


if __name__ == '__main__':
    main()
