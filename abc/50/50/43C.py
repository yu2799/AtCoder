from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    a = list(map(int, input().split()))
    res = float("inf")
    for i in range(-100, 101):
        tmp = 0
        for j in a:
            tmp += (j - i) * (j - i)
        if tmp < res:
            res = tmp
    print(res)


if __name__ == "__main__":
    main()
