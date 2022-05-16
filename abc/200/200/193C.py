from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    tmp = int(n ** 0.5)
    res = set()
    for i in range(2, tmp + 1):
        x = i * i
        while x < n:
            res.add(x)
            x *= i
    print(n - len(res))


if __name__ == '__main__':
    main()
