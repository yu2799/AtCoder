from sys import stdin


def main():
    input = stdin.readline
    k = int(input())
    a, b = input().split()
    print(int(a, k) * int(b, k))


if __name__ == "__main__":
    main()
