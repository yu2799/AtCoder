from sys import stdin


def main():
    input = stdin.readline
    n, s, k = map(int, input().split())
    res = 0
    for _ in range(n):
        p, q = map(int, input().split())
        res += p * q
    if res < s:
        res += k
    print(res)


if __name__ == "__main__":
    main()
