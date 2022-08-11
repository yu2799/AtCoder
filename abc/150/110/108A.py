from sys import stdin


def main():
    input = stdin.readline
    k = int(input())
    print(k * k // 4 if k % 2 == 0 else (k // 2) * (k // 2 + 1))


if __name__ == "__main__":
    main()
