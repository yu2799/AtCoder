from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a, b, c = sorted(map(int, input().split()))
    res = 10000
    for i in range(9999, -1, -1):
        tmp_c = i * c
        if tmp_c > n:
            continue
        for j in range(9999 - i, -1, -1):
            tmp_b = b * j + tmp_c
            if tmp_b > n:
                continue
            if (n - tmp_b) % a == 0:
                k = (n - tmp_b) // a
                res = min(res, i + j + k)
    print(res)


if __name__ == "__main__":
    main()
