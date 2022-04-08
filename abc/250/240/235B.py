from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    h = [int(i) for i in input().split()]
    res = h[0]
    for i in h[1:]:
        if res < i:
            res = i
        else:
            print(res)
            exit()
    else:
        print(res)


if __name__ == '__main__':
    main()
