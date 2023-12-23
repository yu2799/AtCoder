from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    tmp = [set() for _ in range(n)]
    for _ in range(m):
        a = list(map(int, input().split()))
        for i in range(n - 1):
            left = a[i] - 1
            right = a[i + 1] - 1
            tmp[left].add(right)
            tmp[right].add(left)
    res = 0
    for i in tmp:
        res += n - len(i) - 1
    print(res // 2)


if __name__ == "__main__":
    main()
