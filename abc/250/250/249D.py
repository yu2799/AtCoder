from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    a = list(map(int, input().split()))
    MAX = 2 * 10**5
    cnt = [0] * (MAX + 1)
    for i in a:
        cnt[i] += 1

    res = 0
    for i in range(1, MAX + 1):
        j = 1
        while i * j <= MAX:
            res += cnt[i] * cnt[j] * cnt[i * j]
            j = j + 1
    print(res)


if __name__ == "__main__":
    main()
