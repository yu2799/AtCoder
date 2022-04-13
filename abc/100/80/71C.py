from sys import stdin
from collections import defaultdict


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(int)
    tmp = []
    for i in a:
        d[i] += 1
        if d[i] % 2 == 0:
            tmp.append(i)
    if tmp:
        tmp.sort(reverse=True)
        print(tmp[0] * tmp[1])
    else:
        print(0)


if __name__ == '__main__':
    main()
