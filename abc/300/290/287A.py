from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    cnt = 0
    for _ in range(n):
        s = input()[:-1]
        if s == "For":
            cnt += 1
    print("Yes" if n < cnt * 2 else "No")


if __name__ == "__main__":
    main()
