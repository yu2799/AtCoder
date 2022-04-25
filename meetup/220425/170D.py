from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    res = 0
    tmp = [True] * (a[-1] + 1)
    for idx, i in enumerate(a):
        if not tmp[i]:
            continue
        for j in range(i, a[-1] + 1, i):
            tmp[j] = False
        if idx != len(a) - 1 and a[idx] == a[idx + 1]:
            continue
        res += 1
    else:
        print(res)


if __name__ == '__main__':
    main()
