from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    res = 1
    mod = 10 ** 9 + 7
    for _ in [0] * n:
        a = [i for i in map(int, input().split())]
        res = res * sum(a) % mod
    print(res)


if __name__ == '__main__':
    main()
