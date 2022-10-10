from sys import stdin


def main():
    input = stdin.readline
    n, k, a = map(int, input().split())
    tmp = (a - 1 + k % n) % n
    print(n if tmp == 0 else tmp)


if __name__ == "__main__":
    main()
