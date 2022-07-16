from sys import stdin


def main():
    input = stdin.readline
    _, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    sum_a = sum(a)
    cnt = 0
    for i in a:
        if i * m * 4 >= sum_a:
            cnt = cnt + 1
        else:
            break
    print("Yes" if cnt >= m else "No")


if __name__ == "__main__":
    main()
