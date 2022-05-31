from sys import stdin


def main():
    input = stdin.readline
    n = list(input()[:-1])
    res = []
    for i in range(1, 2 ** len(n) - 1):
        a = []
        b = []
        for idx, j in enumerate(bin(i)[2:].zfill(len(n))):
            if j == "0":
                a.append(n[idx])
            else:
                b.append(n[idx])
        a.sort(reverse=True)
        b.sort(reverse=True)
        res.append(int("".join(a)) * int("".join(b)))
    print(max(res))


if __name__ == "__main__":
    main()
