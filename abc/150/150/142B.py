from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    res = 0
    h = list(map(int, input().split()))
    for i in h:
        if i >= k:
            res += 1
    print(res)


if __name__ == "__main__":
    main()
