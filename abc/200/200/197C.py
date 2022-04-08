from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    res = 10 ** 18

    if len(a) == 1:
        print(a[0])
    else:
        for bit in range(2**(n-1)):
            tmp = a[0]
            xor = 0
            for i in range(1, n):
                print((bit >> (i-1)) & 1)
                if (bit >> (i-1)) & 1:
                    xor ^= tmp
                    tmp = 0
                tmp |= a[i]
            xor ^= tmp

            if xor < res:
                res = xor
        print(res)


if __name__ == '__main__':
    main()
