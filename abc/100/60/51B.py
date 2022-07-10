from sys import stdin


def main():
    input = stdin.readline
    k, s = map(int, input().split())
    res = 0
    for x in range(k + 1):
        for y in range(x, k + 1):
            z = s - x - y
            if y <= z <= k:
                if x == y == z:
                    res += 1
                elif x == y or y == z:
                    res += 3
                else:
                    res += 6
    print(res)


if __name__ == "__main__":
    main()
