from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    x = list(map(int, input().split()))
    print(min([sum([(i - j) ** 2 for j in x]) for i in range(1, 101)]))


if __name__ == "__main__":
    main()
