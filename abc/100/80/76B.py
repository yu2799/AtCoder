from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    k = int(input())
    res = 1
    cnt = 0
    while res < k and cnt < n:
        res = res * 2
        cnt = cnt + 1
    if cnt < n:
        res = res + (n - cnt) * k
    print(res)


if __name__ == "__main__":
    main()
