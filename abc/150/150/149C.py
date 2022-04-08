from sys import stdin


def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0 or n == 1:
        return False
    else:
        l = int(pow(n, 0.5)) + 1
        for i in range(3, l, 2):
            if n % i == 0:
                return False
        else:
            return True


def main():
    input = stdin.readline
    x = int(input())
    while True:
        if is_prime(x):
            print(x)
            exit()
        x += 1


if __name__ == "__main__":
    main()
