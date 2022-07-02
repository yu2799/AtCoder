from sys import stdin


def main():
    input = stdin.readline
    n, x = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in [0] * n]
    res = ab[0][0] + ab[0][1] * x
    prev = ab[0][0] + ab[0][1]
    for i in range(1, n):
        if x - i <= 0:
            break
        tmp = prev + ab[i][0] + ab[i][1] * (x - i)
        if tmp < res:
            res = tmp
        prev += ab[i][0] + ab[i][1]
    print(res)


if __name__ == "__main__":
    main()
