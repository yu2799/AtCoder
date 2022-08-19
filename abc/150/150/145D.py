from sys import stdin


def ncr_eu(n, r, mod):
    ret = 1
    if r < n:
        inv = [1]
        for i in range(1, r + 1):
            inv.append(max(1, (-(mod // i) * inv[mod % i]) % mod))
            ret = ret * (n + 1 - i) * inv[i] % mod
    return ret


def main():
    input = stdin.readline
    x, y = map(int, input().split())
    MOD = 10**9 + 7
    for i in range(x + 1):
        tmp = x - i
        if tmp % 2 == 0:
            tmp //= 2
            if 2 * i + tmp == y:
                print(ncr_eu(i + tmp, tmp, MOD))
                return
    print(0)


if __name__ == "__main__":
    main()
