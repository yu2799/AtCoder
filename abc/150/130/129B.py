from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    w = list(map(int, input().split()))
    res = 10000
    for i in range(n):
        tmp = abs(sum(w[:i]) - sum(w[i:]))
        if tmp < res:
            res = tmp
    print(res)


if __name__ == "__main__":
    main()
