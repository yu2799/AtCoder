from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = [i - idx - 1 for idx, i in enumerate(map(int, input().split()))]
    a.sort()
    mid = a[n // 2]
    print(sum([abs(i - mid) for i in a]))


if __name__ == "__main__":
    main()
