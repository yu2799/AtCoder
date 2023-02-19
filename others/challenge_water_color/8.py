from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = [0] * n
    b = [0] * n
    res = float("inf")
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    for enter in a:
        for exit in b:
            tmp = 0
            for k in range(n):
                tmp += abs(enter - a[k])
                tmp += abs(a[k] - b[k])
                tmp += abs(exit - b[k])
            if tmp < res:
                res = tmp
    print(res)


if __name__ == "__main__":
    main()
