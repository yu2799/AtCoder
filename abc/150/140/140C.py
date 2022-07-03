from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    b = list(map(int, input().split()))
    res = b[0] + b[-1]
    for i in range(n - 2):
        if b[i] < b[i + 1]:
            res += b[i]
        else:
            res += b[i + 1]
    print(res)


if __name__ == "__main__":
    main()
