from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()
    res = []
    l = 0
    for r in range(len(t)):
        while l < n and s[l] != t[r]:
            l += 1
            if s[l] != t[r]:
                res.append("No")
        if s[l] == t[r]:
            res.append("Yes")
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
