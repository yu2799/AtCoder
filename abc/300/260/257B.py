from sys import stdin


def main():
    input = stdin.readline
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    for i in l:
        if i == k:
            if a[i - 1] != n:
                a[i - 1] += 1
        else:
            if a[i - 1] + 1 != a[i]:
                a[i - 1] += 1
    print(*a)


if __name__ == "__main__":
    main()
