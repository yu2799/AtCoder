from sys import stdin


def main():
    input = stdin.readline
    x, y, z = map(int, input().split())
    if abs(x) < abs(y):
        print(abs(x))
    elif x * y < 0:
        print(abs(x))
    else:
        if z < 0 < y < x:
            print(-2 * z + x)
        elif 0 < z < y < x:
            print(x)
        elif x < y < z < 0:
            print(-x)
        elif x < y < 0 < z:
            print(2 * z - x)
        else:
            print(-1)


if __name__ == "__main__":
    main()
