from re import A
from sys import stdin


def main():
    input = stdin.readline
    v, *a = map(int, input().split())
    cnt = 0
    while v >= a[cnt]:
        v -= a[cnt]
        cnt += 1
        cnt %= 3
    if cnt == 0:
        print("F")
    elif cnt == 1:
        print("M")
    else:
        print("T")


if __name__ == "__main__":
    main()
