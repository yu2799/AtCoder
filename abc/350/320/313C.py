from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(sorted(map(int, input().split())))
    ave = sum(a) // n
    low = [ave - i for i in a if i <= ave]
    high = [i - ave - 1 for i in a if i > ave]
    print(max(sum(low), sum(high)))


if __name__ == "__main__":
    main()
