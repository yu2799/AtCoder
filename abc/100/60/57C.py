from sys import stdin


def func(a, b):
    a = len(str(a))
    b = len(str(b))
    return max(a, b)


def main():
    input = stdin.readline
    n = int(input())
    res = len(str(n))
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            tmp = func(i, n // i)
            if tmp < res:
                res = tmp
    print(res)


if __name__ == "__main__":
    main()
