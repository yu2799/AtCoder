from sys import stdin


def main():
    input = stdin.readline
    x, y = map(int, input().split())
    for i in range(x + 1):
        if i * 2 + (x - i) * 4 == y:
            print("Yes")
            return
    else:
        print("No")


if __name__ == '__main__':
    main()
