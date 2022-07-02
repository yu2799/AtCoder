from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    res0 = 0
    res1 = 0
    tmp = len(s)
    buf0 = "01" * (tmp // 2) + "0" * (tmp % 2)
    buf1 = "10" * (tmp // 2) + "1" * (tmp % 2)
    for i, j, k in zip(s, buf0, buf1):
        if i != j:
            res0 += 1
        if i != k:
            res1 += 1
    print(res0 if res0 <= res1 else res1)


if __name__ == "__main__":
    main()
