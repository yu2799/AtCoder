from sys import stdin


def main():
    input = stdin.readline
    l, r = map(int, input().split())
    if r - l >= 2019:
        print(0)
        return
    res = 2020
    for i in range(l, r + 1):
        for j in range(i + 1, r + 1):
            if i * j % 2019 < res:
                res = i * j % 2019
                if res == 0:
                    print(0)
                    return
    print(res)


if __name__ == "__main__":
    main()
