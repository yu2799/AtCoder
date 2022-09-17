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
    n = int(input())
    res = []
    buf = bin(n)[2:]
    pos = []
    for idx, i in enumerate(buf):
        if i == "1":
            pos.append(idx)
    for i in bit_exhaustive_seach(pos):
        tmp = list(buf)
        for j in i:
            tmp[j] = "0"
        res.append(int("".join(tmp), 2))
    res.sort()
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
