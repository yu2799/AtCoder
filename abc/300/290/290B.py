from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    s = input()[:-1]
    cnt = 0
    res = ["x"] * n
    for i in range(n):
        res[i] = s[i]
        if s[i] == "o":
            cnt += 1
            if cnt == k:
                print(*res, sep="")
                return


if __name__ == "__main__":
    main()
