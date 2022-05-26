from sys import stdin


def main():
    input = stdin.readline
    a = input()[:-1]
    b = input()[:-1]
    c = input()[:-1]
    a_cnt = 1
    b_cnt = 0
    c_cnt = 0
    a_len = len(a)
    b_len = len(b)
    c_len = len(c)
    prev = a[0]
    while True:
        if prev == "a":
            if a_cnt == a_len:
                print("A")
                return
            prev = a[a_cnt]
            a_cnt += 1
        elif prev == "b":
            if b_cnt == b_len:
                print("B")
                return
            prev = b[b_cnt]
            b_cnt += 1
        else:
            if c_cnt == c_len:
                print("C")
                return
            prev = c[c_cnt]
            c_cnt += 1


if __name__ == "__main__":
    main()
