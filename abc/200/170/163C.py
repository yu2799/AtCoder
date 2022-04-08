from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    res = [0] * n
    for i in a:
        res[i-1] += 1
    print(*res, sep="\n")


if __name__ == '__main__':
    main()
