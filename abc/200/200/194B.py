from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())

    res = 10**5
    for i in range(n):
        for j in range(n):
            res = min(res, a[i] + b[j] if i == j else max(a[i], b[j]))
    print(res)


if __name__ == "__main__":
    main()
