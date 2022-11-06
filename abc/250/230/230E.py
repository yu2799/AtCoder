from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    res = 0
    for i in range(1, int(n**0.5) + 1):
        res += n // i
    print(res * 2 - int(n**0.5) ** 2)


if __name__ == "__main__":
    main()
