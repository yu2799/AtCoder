from sys import stdin


def cross(x1, y1, x2, y2):
    return x1 * y2 - x2 * y1


def is_convex(n, vertexes):
    for i in range(n):
        a = vertexes[i % n]
        b = vertexes[(i + 1) % n]
        c = vertexes[(i + 2) % n]

        vec_ab = [b[0] - a[0], b[1] - a[1]]
        vec_bc = [c[0] - b[0], c[1] - b[1]]

        if cross(*vec_ab, *vec_bc) < 0:
            return False
    return True


def main():
    input = stdin.readline
    xy = [tuple(map(int, input().split())) for _ in range(4)]
    print("Yes" if is_convex(4, xy) else "No")


if __name__ == "__main__":
    main()
