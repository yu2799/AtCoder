from sys import stdin


def main():
    input = stdin.readline
    x = {i: chr(65 + idx) for idx, i in enumerate(list(input()[:-1]))}
    n = int(input())
    s = [input()[:-1] for _ in [0] * n]
    s.sort(key=lambda s: "".join(x[c] for c in list(s)))
    print(*s, sep="\n")


if __name__ == "__main__":
    main()
