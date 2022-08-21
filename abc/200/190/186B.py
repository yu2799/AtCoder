from sys import stdin


def main():
    input = stdin.readline
    h, w = map(int, input().split())
    a = []
    for _ in [0] * h:
        for i in map(int, input().split()):
            a.append(i)
    print(sum(a) - min(a) * h * w)


if __name__ == "__main__":
    main()
