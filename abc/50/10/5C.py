from sys import stdin


def main():
    input = stdin.readline
    t = int(input())
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    ai, bi = 0, 0
    while ai < n and bi < m:
        if a[ai] <= b[bi] <= a[ai] + t:
            ai += 1
            bi += 1
        else:
            ai += 1
    print("yes" if bi == m else "no")


if __name__ == "__main__":
    main()
