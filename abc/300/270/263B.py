from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    p = list(map(int, input().split()))
    res = 1
    parent = p[n - 2]
    while parent != 1:
        parent = p[parent - 2]
        res += 1
    print(res)


if __name__ == "__main__":
    main()
