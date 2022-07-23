from sys import stdin


def main():
    input = stdin.readline
    n, m, x = map(int, input().split())
    a = list(map(int, input().split()))
    tmp = 0
    for i in a:
        if i < x:
            tmp = tmp + 1
        else:
            print(min(tmp, m - tmp))
            return


if __name__ == "__main__":
    main()
