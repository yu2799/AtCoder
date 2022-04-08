from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    print(sum(abs(i-j) for i, j in zip(a, b)))


if __name__ == '__main__':
    main()
