from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    d = list(map(int, input().split()))
    res = 0
    for i in range(1, n + 1):
        for j in range(1, d[i - 1] + 1):
            if len(set(list(f"{i}{j}"))) == 1:
                res += 1
    print(res)


if __name__ == "__main__":
    main()
