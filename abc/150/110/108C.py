from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    cnt = 0
    for i in range(1, n + 1):
        if i % k == 0:
            cnt = cnt + 1
    res = cnt * cnt * cnt

    if k % 2 == 0:
        cnt = 0
        for i in range(1, n + 1):
            if i % k == k // 2:
                cnt = cnt + 1
        res = res + cnt * cnt * cnt
    print(res)


if __name__ == "__main__":
    main()
