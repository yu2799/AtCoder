from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    v = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    res = 0
    for i, j in zip(v, c):
        tmp = i - j
        if tmp > 0:
            res += tmp
    print(res)

if __name__ == '__main__':
    main()