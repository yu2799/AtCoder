from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    v = [] * n
    for _ in [0] * m:
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a
        v[b - 1] += 1
    print(v.count(1))


if __name__ == '__main__':
    main()
