from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    print(max(a)-min(a))


if __name__ == '__main__':
    main()
