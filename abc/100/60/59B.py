from sys import stdin


def main():
    input = stdin.readline
    a = input()[:-1]
    b = input()[:-1]
    len_a = len(a)
    len_b = len(b)
    if len_a > len_b:
        print("GREATER")
    elif len_b > len_a:
        print("LESS")
    else:
        if a == b:
            print("EQUAL")
        else:
            for i in range(len_a):
                if a[i] > b[i]:
                    print("GREATER")
                    return
                else:
                    print("LESS")
                    return


if __name__ == "__main__":
    main()
