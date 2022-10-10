from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    s = list(map(int, input().split()))
    res = 0
    for i in s:
        for a in range(1, 201):
            for b in range(1, 201):
                if 4 * a * b + 3 * (a + b) == i:
                    break
            else:
                continue
            break
        else:
            res += 1
    print(res)


if __name__ == "__main__":
    main()
