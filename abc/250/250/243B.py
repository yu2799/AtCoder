from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    res1 = 0
    res2 = 0
    for i, j in zip(a, b):
        if i == j:
            res1 += 1
    for i in a:
        for j in b:
            if i == j:
                res2 += 1
    print(res1)
    print(res2 - res1)


if __name__ == "__main__":
    main()
