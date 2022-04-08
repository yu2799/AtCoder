a, b, c = map(int, input().split())
mod = 998244353
res = (a*(a+1)*b*(b+1)*c*(c+1)//8)
print(res%mod)