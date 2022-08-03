from sys import stdin


def main():
    input = stdin.readline
    a, b, c, k = map(int, input().split())
    if k <= a:
        print(k)
    elif k <= a + b:
        print(a)
    elif k <= a + b + c:
        print(a - (k - a - b))
    else:
        print(a - c)


if __name__ == "__main__":
    main()
