from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    for i in range(1, 38):
        for j in range(1, 26):
            if 3 ** i + 5 ** j == n:
                print(i, j)
                return
    print(-1)


if __name__ == '__main__':
    main()
