from math import atan2, sqrt, pi, cos, sin


n = int(input())
x0, y0 = map(int, input().split())
xh, yh = map(int, input().split())
cx, cy = (x0 + xh) / 2, (y0 + yh) / 2
theta = atan2((y0-cy), (x0-cx)) + 2 * pi / n
r = sqrt((cx-x0)**2 + (cy-y0)**2)
print(cx+r*cos(theta), cy+r*sin(theta))
