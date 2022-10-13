from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    tmp = [set() for _ in [0] * (m + 1)]
    res = []
    for idx, i in enumerate(a):
        left = 1 if i >= 0 else (-i + idx) // (idx + 1)
        right = min(m + 1, (n - i + idx) // (idx + 1))
        for j in range(left, right):
            tmp[j].add(i + (idx + 1) * j)

    for i in tmp[1:]:
        for j in range(n + 1):
            if j not in i:
                res.append(j)
                break
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
