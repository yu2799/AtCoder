from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    a = list(map(int, input().split()))
    d = {}
    gar = 0
    for i in a:
        if i in d:
            gar += 1
        else:
            d[i] = 0
    tmp = sorted(d.keys())
    left = 0
    right = len(tmp)
    res = 0
    while left < right or gar != 0:
        if res + 1 in d:
            left += 1
            res += 1
        else:
            if gar >= 2:
                res += 1
                gar -= 2
            elif gar == 1:
                gar -= 1
                if left <= right - 1:
                    res += 1
                    right -= 1
                else:
                    break
            else:
                if left <= right - 2:
                    res += 1
                    right -= 2
                else:
                    break

    print(res)


if __name__ == "__main__":
    main()
