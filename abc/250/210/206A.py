import math
n = float(input())
if math.floor(n * 1.08) < 206:
    print("Yay!")
elif math.floor(n * 1.08) > 206:
    print(":(")
else:
    print("so-so")
