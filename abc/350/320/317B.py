from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(1, n):
        if a[i] != a[i - 1] + 1:
            print(a[i - 1] + 1)
            return


if __name__ == "__main__":
    main()
