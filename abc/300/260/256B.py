from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        for j in range(n - 1, i, -1):
            a[i] += a[j]
    print(sum([1 for i in a if i >= 4]))


if __name__ == "__main__":
    main()
