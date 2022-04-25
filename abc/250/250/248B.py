from sys import stdin


def main():
    input = stdin.readline
    a, b, k = map(int, input().split())
    res = 0
    while a < b:
        res += 1
        a *= k
    print(res)


if __name__ == '__main__':
    main()
