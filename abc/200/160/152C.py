from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    p = list(map(int, input().split()))
    tmp = n + 1
    res = 0
    for i in p:
        if i < tmp:
            res += 1
            tmp = i
    print(res)


if __name__ == "__main__":
    main()
