from sys import stdin


def main():
    input = stdin.readline
    left, right = map(int, input().split())
    right = min(left + 2019, right) + 1
    res = float("inf")
    for i in range(left, right):
        for j in range(i + 1, right):
            tmp = (i % 2019) * (j % 2019) % 2019
            if tmp < res:
                res = tmp
    print(res)


if __name__ == "__main__":
    main()
