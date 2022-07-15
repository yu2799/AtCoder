from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = [int(input()) - 1 for _ in [0] * n]
    flag = [False] * n
    i = 0
    res = 0
    for _ in [0] * n:
        if i == 1:
            print(res)
            return
        flag[i] = True
        i = a[i]
        res += 1
    print(-1)


if __name__ == "__main__":
    main()
