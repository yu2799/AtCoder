from sys import stdin


def cmb(n, r, mod, g1, g2):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    MOD = 10**9 + 7
    g1 = [1, 1]
    g2 = [1, 1]
    inverse = [0, 1]

    for i in range(2, n + 1):
        g1.append((g1[-1] * i) % MOD)
        inverse.append((-inverse[MOD % i] * (MOD // i)) % MOD)
        g2.append((g2[-1] * inverse[-1]) % MOD)
    res = []
    for i in range(1, k + 1):
        res.append(
            cmb(k - 1, i - 1, MOD, g1, g2)
            * cmb(n - k + 1, i, MOD, g1, g2)
            % MOD
        )
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
