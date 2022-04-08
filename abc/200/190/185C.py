from sys import stdin


def main():
    input = stdin.readline
    l = int(input())
    res = 1
    for i in range(11):
        res = res * (l - i - 1) // (i + 1)
    print(res)


if __name__ == "__main__":
    main()
