from sys import stdin


def bit_exhaustive_seach(product_list):
    n = len(product_list)
    res = []
    for i in range(1 << n):
        tmp = []
        for j in range(n):
            if i >> j & 1:
                tmp.append(product_list[j])
        res.append(tmp)
    return res


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a = []
    for _ in range(m):
        _ = int(input())
        tmp = set(map(int, input().split()))
        a.append(tmp)

    res = 0
    for i in bit_exhaustive_seach(range(m)):
        if not i:
            continue
        tmp = set()
        for j in i:
            tmp |= a[j]
        for j in range(1, n + 1):
            if j not in tmp:
                break
        else:
            res += 1
    print(res)


if __name__ == "__main__":
    main()
