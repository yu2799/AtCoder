from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    max_ind = a.index(max(a))
    a[max_ind] = 0
    print(a.index(max(a)) + 1)


if __name__ == "__main__":
    main()
