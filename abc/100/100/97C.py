from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    k = int(input())
    res = set()
    s_len = len(s)
    for i in range(s_len):
        for j in range(1, 6):
            if i + j <= s_len:
                res.add(s[i : i + j])
            else:
                break

    print(sorted(list(res))[k - 1])


if __name__ == "__main__":
    main()
