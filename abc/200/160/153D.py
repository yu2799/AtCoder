from sys import stdin


def main():
    input = stdin.readline
    h = int(input())
    cnt = 0
    while h > 0:
        h //= 2
        cnt += 1
    print(2 ** cnt - 1)


if __name__ == "__main__":
    main()
