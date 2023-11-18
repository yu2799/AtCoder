from sys import stdin


def main():
    input = stdin.readline
    m = int(input())
    d = list(map(int, input().split()))
    mid = (sum(d) + 1) // 2
    a = 0
    cnt = 0
    while True:
        if d[a] + cnt < mid:
            cnt += d[a]
            a += 1
        else:
            print(a + 1, mid - cnt)
            return


if __name__ == "__main__":
    main()
