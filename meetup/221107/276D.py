from sys import stdin


def calc(n):
    two_cnt = 0
    three_cnt = 0
    while n % 2 == 0:
        n //= 2
        two_cnt += 1
    while n % 3 == 0:
        n //= 3
        three_cnt += 1
    return [n, two_cnt, three_cnt]


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    prev, two_min, three_min = calc(a[0])
    cnt = two_min + three_min
    for i in a[1:]:
        tmp, two_cnt, three_cnt = calc(i)
        if tmp != prev:
            print(-1)
            return
        two_min = min(two_min, two_cnt)
        three_min = min(three_min, three_cnt)
        cnt += two_cnt + three_cnt
    print(cnt - two_min * n - three_min * n)


if __name__ == "__main__":
    main()
