from sys import stdin


def main():
    input = stdin.readline
    _, k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort(reverse=True)
    print(sum(h[k:]))


if __name__ == "__main__":
    main()
