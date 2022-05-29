from sys import stdin
from math import gcd


def main():
    input = stdin.readline
    n, a, b = map(int, input().split())
    res = n * (n + 1) // 2
    tmp_a = (n // a) * (a + (n // a) * a) // 2
    tmp_b = (n // b) * (b + (n // b) * b) // 2
    lcm = a * b // gcd(a, b)
    tmp_c = (n // lcm) * (lcm + (n // lcm) * lcm) // 2

    print(res - tmp_a - tmp_b + tmp_c)


if __name__ == "__main__":
    main()
