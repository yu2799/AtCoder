from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = [i for i in map(int, input().split())]
    res = 0
    l = 0
    tmp = 0
    for r in a:
        if l < r:
            tmp += 1
        else:
            tmp = 1
        l = r
        res += tmp
    print(res)


if __name__ == "__main__":
    main()
