from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    l = sum(a)
    cnt = 0
    for i in a:
        if i * m * 4 >= l:
            cnt += 1
        if cnt == m:
            print("Yes")
            return
    else:
        print("No")


if __name__ == "__main__":
    main()
