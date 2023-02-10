from sys import stdin


def main():
    input = stdin.readline
    _, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    prev_a = a[0]
    prev_b = b[0]
    for i, j in zip(a[1:], b[1:]):
        if prev_a and prev_b:
            ok_a = i if abs(prev_a - i) <= k or abs(prev_b - i) <= k else 0
            ok_b = j if abs(prev_a - j) <= k or abs(prev_b - j) <= k else 0
        elif prev_a:
            ok_a = i if abs(prev_a - i) <= k else 0
            ok_b = j if abs(prev_a - j) <= k else 0
        elif prev_b:
            ok_a = i if abs(prev_b - i) <= k else 0
            ok_b = j if abs(prev_b - j) <= k else 0

        if not (ok_a or ok_b):
            print("No")
            return
        prev_a = ok_a
        prev_b = ok_b
    print("Yes")


if __name__ == "__main__":
    main()
