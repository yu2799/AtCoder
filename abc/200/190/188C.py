from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    left = a[: 2 ** (n - 1)]
    max_l = max(left)
    idx_l = left.index(max_l) + 1
    right = a[2 ** (n - 1) :]
    max_r = max(right)
    idx_r = right.index(max_r) + 1 + 2 ** (n - 1)
    print(idx_l if max_l < max_r else idx_r)


if __name__ == "__main__":
    main()
