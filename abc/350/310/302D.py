from sys import stdin


def main():
    input = stdin.readline
    n, m, d = map(int, input().split())
    a = list(sorted(map(int, input().split())))
    b = list(sorted(map(int, input().split())))
    i = n - 1
    j = m - 1
    while i >= 0 and j >= 0:
        if abs(a[i] - b[j]) <= d:
            print(a[i] + b[j])
            return
        if a[i] > b[j]:
            i -= 1
        else:
            j -= 1
    print(-1)


if __name__ == "__main__":
    main()
