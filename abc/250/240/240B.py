from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = set(int(i) for i in input().split())
    print(len(a))


if __name__ == "__main__":
    main()
