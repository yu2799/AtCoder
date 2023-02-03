from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    if 2 * n >= m:
        res = m // 2
    else:
        res = n
        m -= 2 * res
        res += m // 4
    print(res)


if __name__ == "__main__":
    main()
