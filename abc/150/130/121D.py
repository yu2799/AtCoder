from sys import stdin


def main():
    input = stdin.readline
    a, b = map(int, input().split())
    digit = len(bin(b)[2:])
    b += 1
    res = []
    for i in range(1, digit + 1):
        tmp = 2**i
        cnt = ((b // tmp) * (tmp // 2) + max(0, (b % tmp) - (tmp // 2))) - (
            (a // tmp) * (tmp // 2) + max(0, (a % tmp) - (tmp // 2))
        )
        res.append(str(cnt % 2))
    res.reverse()
    print(int("".join(res), 2))


if __name__ == "__main__":
    main()
