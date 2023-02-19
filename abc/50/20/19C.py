from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    a = set(map(int, input().split()))
    res = len(a)
    for i in a:
        tmp = i
        while tmp % 2 == 0:
            tmp //= 2
            if tmp in a:
                res -= 1
                break
    print(res)


if __name__ == "__main__":
    main()
