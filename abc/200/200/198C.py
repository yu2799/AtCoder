import math
r, x, y = map(int, input().split())
dist = math.sqrt(pow(x, 2) + pow(y, 2))
if dist < r:
    print(2)
else:
    print(math.ceil(dist/r))