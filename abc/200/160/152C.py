from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    p = list(map(int, input().split()))
    res = 0
    tmp = float("inf")
    for i in p:
        if tmp > i:
            tmp = i
            res += 1
    print(res)


if __name__ == "__main__":
    main()
