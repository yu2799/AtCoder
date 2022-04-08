from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    ab = sorted([list(map(int, input().split()))
                for _ in [0] * n], key=lambda x: -x[1])
    cd = sorted([list(map(int, input().split())) for _ in [0] * n])
    res = 0

    for a, b in ab:
        for i in range(n):
            if a < cd[i][0] and b < cd[i][1]:
                cd[i][0], cd[i][1] = 0, 0
                res += 1
                break
    print(res)


if __name__ == '__main__':
    main()
