from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    h = [int(i) for i in input().split()]
    res = 0
    prev = 0
    tmp = 0
    for i in h:
        if prev >= i:
            tmp += 1
        else:
            if tmp > res:
                res = tmp
            tmp = 0
        prev = i
    print(max(tmp, res))


if __name__ == "__main__":
    main()
