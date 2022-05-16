from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a = 1
    b = n
    for _ in [0] * m:
        l, r = map(int, input().split())
        if a < l:
            a = l
        if r < b:
            b = r
    print(b - a + 1 if a <= b else 0)


if __name__ == "__main__":
    main()
