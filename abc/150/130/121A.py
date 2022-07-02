from sys import stdin


def main():
    input = stdin.readline
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    print(H * W - (W * h + H * w) + h * w)


if __name__ == "__main__":
    main()
