from sys import stdin


def score(s):
    d = [0] * 10
    for c in s:
        d[int(c)] += 1
    return sum([i * 10 ** d[i] for i in range(1, 10)])


def main():
    input = stdin.readline
    k = int(input())
    s = input()[:-2]
    t = input()[:-2]
    d = {i: k for i in range(1, 10)}
    for i, j in zip(s, t):
        d[int(i)] -= 1
        d[int(j)] -= 1

    res = 0
    for i in range(1, 10):
        if d[i] == 0:
            continue
        for j in range(1, 10):
            if i == j or d[j] == 0:
                continue
            if score(s + str(i)) > score(t + str(j)):
                res += d[i] * d[j]

    for i in range(1, 10):
        if d[i] < 2:
            continue
        if score(s + str(i)) > score(t + str(i)):
            res += d[i] * (d[i] - 1)
    print(res / (9 * k - 8) / (9 * (k - 1)))


if __name__ == "__main__":
    main()
