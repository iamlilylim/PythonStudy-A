t = int(input())

wrd = list(set(input() for _ in range(t)))
wrd.sort(key=lambda x: (len(x), x))
for wr in wrd:
    print(wr)