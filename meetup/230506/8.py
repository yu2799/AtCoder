from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    res = a[0]
    if n % 2 == 0:
        res += 2 * sum(a[1 : n // 2])
    else:
        res += 2 * sum(a[1 : (n - 1) // 2]) + a[(n - 1) // 2]
    print(res)


if __name__ == "__main__":
    main()
