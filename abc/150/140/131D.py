from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    ab = [list(map(int, input().split())) for _ in [0] * n]
    ab.sort(key=lambda x: x[1])
    t = 0
    for a, b in ab:
        t += a
        if t > b:
            print("No")
            exit()
    print("Yes")


if __name__ == '__main__':
    main()
