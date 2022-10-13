from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    res = [0] * n
    for x in range(1, 101):
        for y in range(1, 101):
            for z in range(1, 101):
                tmp = x * x + y * y + z * z + x * y + y * z + z * x
                if tmp <= n:
                    res[tmp - 1] += 1
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
