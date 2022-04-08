# used pypy3
from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a, b, c = sorted(map(int, input().split()))
    res = 9999
    for i in range(res+1):
        tmp = i * c
        for j in range(res-i+1):
            m = n - tmp - j*b
            if m < 0:
                break
            if m % a == 0:
                k = m // a
                if i + j + k < res:
                    res = i + j + k
    print(res)


if __name__ == '__main__':
    main()
