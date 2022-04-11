from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    cnt_4 = 0
    cnt_2 = 0
    for i in a:
        if i % 4 == 0:
            cnt_4 += 1
        elif i % 2 == 0:
            cnt_2 += 1
    print("Yes" if n // 2 <= cnt_4 + cnt_2 // 2 else "No")


if __name__ == '__main__':
    main()
