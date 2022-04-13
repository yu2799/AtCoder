from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(set(map(int, input().split())))
    l = len(a)
    print(l if l % 2 else l-1)


if __name__ == '__main__':
    main()
