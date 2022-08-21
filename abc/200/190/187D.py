from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a_tot = 0
    tmp = []
    res = 0
    for _ in [0] * n:
        a, b = map(int, input().split())
        a_tot += a
        tmp.append(a + a + b)
    tmp.sort()
    while 0 <= a_tot:
        a_tot -= tmp.pop()
        res += 1
    print(res)


if __name__ == "__main__":
    main()
