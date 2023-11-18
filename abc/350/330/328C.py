from sys import stdin


def main():
    input = stdin.readline
    n, q = map(int, input().split())
    s = input()[:-1]
    accm = [0] * n
    for i in range(1, n):
        if s[i - 1] == s[i]:
            accm[i] += 1
        accm[i] += accm[i - 1]
    res = []
    for _ in range(q):
        left, right = map(lambda x: int(x) - 1, input().split())
        res.append(accm[right] - accm[left])
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
