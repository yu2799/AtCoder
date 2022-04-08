from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    for i in range(int(pow(n, 0.5)), 0, -1):
        if n % i == 0:
            print(n // i + i - 2)
            exit()


if __name__ == "__main__":
    main()
