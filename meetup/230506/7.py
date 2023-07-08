from sys import stdin


def main():
    input = stdin.readline
    n, q = map(int, input().split())
    s = input()[:-1]
    res = []
    cnt = [0] * n
    for i in range(1, n):
        cnt[i] = cnt[i - 1]
        if s[i - 1] == "A" and s[i] == "C":
            cnt[i] += 1
    for _ in range(q):
        left, right = map(lambda x: int(x) - 1, input().split())
        res.append(cnt[right] - cnt[left])
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
