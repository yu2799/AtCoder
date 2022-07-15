from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in [0] * n]
    ab.sort()
    tmp = []
    head = 1
    for a, b in ab:
        tmp.append((a, head))
        head += b
    prev = tmp[0]
    for i in tmp[1:]:
        if k < i[1]:
            print(prev[0])
            return
        prev = i
    print(prev[0])


if __name__ == "__main__":
    main()
