from sys import stdin


def main():
    input = stdin.readline
    x, y, *_ = map(int, input().split())
    p = [int(i) for i in input().split()]
    q = [int(i) for i in input().split()]
    r = [int(i) for i in input().split()]
    p.sort(reverse=True)
    q.sort(reverse=True)
    l = p[:x] + q[:y] + r
    l.sort(reverse=True)
    print(sum(l[: x + y]))


if __name__ == "__main__":
    main()
