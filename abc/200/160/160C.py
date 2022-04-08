from sys import stdin


def main():
    input = stdin.readline
    k, n = map(int, input().split())
    a = [int(i) for i in input().split()]
    d = k + a[0] - a[-1]
    y = a[0]
    for x in a[1:]:
        dis = x - y
        if d < dis:
            d = dis
        y = x
    print(k - d)


if __name__ == "__main__":
    main()
