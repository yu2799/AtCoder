from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print(sum(a[::2]) - sum(a[1::2]))


if __name__ == "__main__":
    main()
