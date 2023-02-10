from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    res = [False] * 2001
    a = list(map(int, input().split()))
    for i in a:
        res[i] = True
    for i in range(2001):
        if not res[i]:
            print(i)
            return


if __name__ == "__main__":
    main()
