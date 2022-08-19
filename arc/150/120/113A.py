from sys import stdin


def main():
    input = stdin.readline
    k = int(input())
    res = 0
    for i in range(1, k + 1):
        if i * i * i > k:
            break
        for j in range(i, k + 1):
            if i * j * j > k:
                break
            tmp = k // (i * j)
            if tmp < j:
                continue
            if i == j:
                res += 1 + 3 * (tmp - j)
            else:
                res += 3 + 6 * (tmp - j)
    print(res)


if __name__ == "__main__":
    main()
