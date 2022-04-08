from sys import stdin


def eight_to_ten(n):
    res = 0
    l = len(n)
    for i in range(l):
        res += int(n[i]) * 8 ** (l - i - 1)
    return res


def ten_to_nine(n):
    res = ""
    while n > 0:
        res += str(n % 9)
        n //= 9
    return res[::-1]


def main():
    input = stdin.readline
    n, k = input().split()
    for _ in [0] * int(k):
        n = ten_to_nine(eight_to_ten(n)).replace("8", "5", 10**18)
    print(n)


if __name__ == '__main__':
    main()
