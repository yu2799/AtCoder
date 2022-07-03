from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    a, b, c = [list(map(int, input().split())) for _ in [0] * 3]
    res = b[a[0] - 1]
    prev = a[0] - 1
    for i in a[1:]:
        res += b[i - 1]
        if prev + 1 == i - 1:
            res += c[prev]
        prev = i - 1
    print(res)


if __name__ == "__main__":
    main()
