from sys import stdin


def my_round_int(x):
    return int((x * 2 + 1) // 2)


def main():
    input = stdin.readline
    x, k = map(int, input().split())
    for _ in range(k):
        x = my_round_int(x / 10)
    print(x * pow(10, k))


if __name__ == "__main__":
    main()
