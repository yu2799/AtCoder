from sys import stdin


def main():
    input = stdin.readline
    *x, = map(int, input().split())
    for i in range(len(x)):
        if x[i] == 0:
            print(i + 1)


if __name__ == '__main__':
    main()