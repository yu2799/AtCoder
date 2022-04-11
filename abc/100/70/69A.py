from sys import stdin


def main():
    input = stdin.readline
    n, m = [int(i) - 1 for i in input().split()]
    print(n * m)

if __name__ == '__main__':
    main()