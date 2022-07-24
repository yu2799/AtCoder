from sys import stdin


def main():
    input = stdin.readline
    l1, r1, l2, r2 = map(int, input().split())
    a = list(sorted([[l1, r1], [l2, r2]]))
    if a[1][0] <= a[0][1]:
        if a[1][1] <= a[0][1]:
            print(a[1][1] - a[1][0])
        else:
            print(a[0][1] - a[1][0])
    else:
        print(0)


if __name__ == "__main__":
    main()
