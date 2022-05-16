from sys import stdin
from operator import itemgetter


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    tmp = []
    for _ in [0] * m:
        b, c = map(int, input().split())
        tmp.append((b, c))
    tmp.sort(key=itemgetter(1), reverse=True)
    res = []
    cnt = 0
    for i in tmp:
        cnt += i[0]
        res += [i[1]] * i[0]
        if n <= cnt:
            break
    res += a
    res.sort(reverse=True)
    print(sum(res[:n]))


if __name__ == "__main__":
    main()
