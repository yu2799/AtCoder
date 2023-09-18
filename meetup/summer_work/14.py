from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    tmp = set()
    for i in range(2, int(pow(n, 0.5)) + 1):
        num = i * i
        while num <= n:
            tmp.add(num)
            num *= i
    print(n - len(tmp))


if __name__ == "__main__":
    main()
