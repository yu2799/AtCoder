from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    a = list(map(int, input().split()))
    _ = int(input())
    b = set(map(int, input().split()))
    x = int(input())
    dp = [False] * (x + 1)
    dp[0] = True
    mini = 0
    while True:
        tmp = x
        pos = []
        for i in range(x, mini - 1, -1):
            if dp[i]:
                pos.append(i)
        if not pos:
            print("No")
            return
        for i in reversed(pos):
            for j in a:
                if i + j <= x and i + j not in b:
                    dp[i + j] = True
                    tmp = min(tmp, i + j)
            dp[i] = False
        if dp[x]:
            print("Yes")
            return
        mini = tmp


if __name__ == "__main__":
    main()
