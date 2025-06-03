n = int(input())
k = list(map(int,input().split()))
m = max(k)
gr = sum(k)/m*100/n
print(gr)