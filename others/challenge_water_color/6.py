from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    s = input()[:-1]
    res = 0
    for i in range(10):
        idx_i = s.find(str(i))
        if idx_i == -1 or n - 2 <= idx_i:
            continue
        for j in range(10):
            idx_j = s.find(str(j), idx_i + 1)
            if idx_j == -1 or n - 1 <= idx_j:
                continue
            for k in range(10):
                if s.find(str(k), idx_j + 1) != -1:
                    res += 1
    print(res)


if __name__ == "__main__":
    main()
