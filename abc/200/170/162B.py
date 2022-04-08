from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    res = 0
    for i in range(1, n + 1):
        if i % 3 and i % 5:
            res += i
    print(res)


if __name__ == "__main__":
    main()
