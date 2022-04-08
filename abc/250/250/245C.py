from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    prev_a = a[0]
    prev_b = b[0]
    for i, j in zip(a[1:], b[1:]):
        flag = False
        if prev_a and prev_b:
            if abs(prev_a - i) <= k or abs(prev_b - i) <= k:
                flag = True
            if abs(prev_a - j) <= k or abs(prev_b - j) <= k:
                prev_b = j
            else:
                prev_b = 0
            if flag:
                prev_a = i
            else:
                prev_a = 0
        elif prev_a:
            if abs(prev_a - i) <= k:
                flag = True
            if abs(prev_a - j) <= k:
                prev_b = j
            else:
                prev_b = 0
            if flag:
                prev_a = i
            else:
                prev_a = 0
        else:
            if abs(prev_b - i) <= k:
                prev_a = i
            else:
                prev_a = 0
            if abs(prev_b - j) <= k:
                prev_b = j
            else:
                prev_b = 0
        if not prev_a and not prev_b:
            print("No")
            return
    else:
        print("Yes")


if __name__ == "__main__":
    main()
