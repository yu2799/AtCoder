from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = [int(i) for i in input().split()]
    res = 0
    min = 10 ** 9 + 1
    cnt = 0
    for i in a:
        tmp = abs(i)
        res += tmp
        if tmp < min:
            min = tmp
        if i < 0:
            cnt += 1
    if cnt % 2 == 0 or 0 in a:
        print(res)
    else:
        print(res - 2 * min)


if __name__ == "__main__":
    main()
