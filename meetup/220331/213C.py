from sys import stdin


def main():
    input = stdin.readline
    h, w, n = map(int, input().split())
    a = []
    b = []
    for _ in [0] * n:
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    adict = {x: i + 1 for i, x in enumerate(sorted(list(set(a))))}
    bdict = {y: i + 1 for i, y in enumerate(sorted(list(set(b))))}

    for i in range(n):
        print(adict[a[i]], bdict[b[i]])


if __name__ == "__main__":
    main()
