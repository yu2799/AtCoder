from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(set(map(int, input().split())))
    a.sort()
    for i in range(2001):
        if not i in a:
            print(i)
            return


if __name__ == "__main__":
    main()
