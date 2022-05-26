from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    m = max(a)
    res = []
    for idx, i in enumerate(a):
        if i == m:
            res.append(idx + 1)
    for i in res:
        if i in b:
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    main()
