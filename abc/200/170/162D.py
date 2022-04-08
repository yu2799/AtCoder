from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    s = input()[:-1]
    r = s.count("R")
    g = s.count("G")
    b = s.count("B")
    res = r * g * b
    for i in range(n):
        for j in range(i + 1, n):
            k = 2 * j - i
            if k < n:
                if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                    res -= 1
            else:
                break
    print(res)


if __name__ == "__main__":
    main()
