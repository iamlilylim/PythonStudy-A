import sys

n = int(sys.stdin.readline())

k = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline().strip())

l = list(map(int,sys.stdin.readline().split()))

for i in l:
    if i in k:

        print(1)
    else:
        print("0")