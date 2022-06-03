from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    res = abs(t - h[0] * 0.006 - a)
    idx = 0
    for i in range(n):
        if res > abs(t - h[i] * 0.006 - a):
            res = abs(t - h[i] * 0.006 - a)
            idx = i
    print(idx + 1)


if __name__ == "__main__":
    main()
