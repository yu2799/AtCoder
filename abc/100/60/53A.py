from sys import stdin


def main():
    input = stdin.readline
    x = int(input())
    print("ABC" if x < 1200 else "ARC")


if __name__ == '__main__':
    main()