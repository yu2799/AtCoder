from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    h = [int(i) for i in input().split()]
    h.sort(reverse=True)
    print(sum(h[k:]))


if __name__ == "__main__":
    main()
