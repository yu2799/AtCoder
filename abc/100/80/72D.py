from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    p = [int(i) for i in input().split()]
    res = 0
    l = 0
    r = len(p)
    while l < r:
        if p[l] == l + 1:
            res += 1
            l += 1
        l += 1
    print(res)


if __name__ == "__main__":
    main()
