from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    a = [[j, i + 1] for i, j in enumerate(map(int, input().split()))]
    a.sort(reverse=True)
    for i in a:
        print(i[1])


if __name__ == "__main__":
    main()
