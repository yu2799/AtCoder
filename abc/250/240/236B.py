from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = [i for i in map(int, input().split())]
    cnt = [0] * (n + 1)
    tmp = 10 ** 5 + 1
    res = 0
    for i in a:
        cnt[i] += 1
    for i in range(1, n + 1):
        if tmp > cnt[i]:
            tmp = cnt[i]
            res = i
    print(res)


if __name__ == "__main__":
    main()
