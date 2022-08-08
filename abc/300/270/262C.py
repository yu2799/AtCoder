from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    a = {idx + 1: i for idx, i in enumerate(map(int, input().split()))}
    res = 0
    cnt = 0
    for i, j in a.items():
        if i == j:
            cnt += 1
        elif a[i] == j and a[j] == i and i < j:
            res += 1
    print(res + (cnt * (cnt - 1)) // 2)


if __name__ == "__main__":
    main()
