from sys import stdin


def main():
    input = stdin.readline
    n, x = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    res = [0] * (n + 1)
    tmp = x
    while not res[tmp]:
        res[tmp] = 1
        tmp = a[tmp]
    print(res.count(1))


if __name__ == '__main__':
    main()
