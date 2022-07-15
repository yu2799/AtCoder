from sys import stdin
from collections import defaultdict


def main():
    input = stdin.readline
    _ = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(int)
    for i in a:
        d[i] += 1

    cnt = 0
    for i in sorted(d.keys(), reverse=True):
        if d[i] >= 2:
            if cnt == 0:
                if d[i] >= 4:
                    print(i * i)
                    return
                else:
                    cnt += 1
                    res = i
            else:
                print(res * i)
                return
    print(0)


if __name__ == "__main__":
    main()
