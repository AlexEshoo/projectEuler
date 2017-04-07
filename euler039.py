from eulerTools import gcd
import json

triples  = {}
for i in range(1,1001):
    triples[i] = []

for n in range(1,32):
    for m in range(n+1,32):
        if not gcd(m,n) == 1:
            continue
        if (m % 2 != 0) and (n % 2 != 0):
            continue
        if n >= m:
            continue
        for k in range(1,201):
            a = k * (m**2 - n**2)
            b = k * 2 * n * m
            c = k * (m**2 + n**2)
            
            p = a + b + c
            
            if p > 1000:
                continue # not sure is break is appropriate... does exceeding it once garuntee you will keepe xceding for different ks?
                
            triples[p].append((a,b,c))

win = 0
count = 0
for key in triples:
    if len(triples[key]) > count:
        count = len(triples[key])
        win = key

print "winner:", win

with open('output.json','w') as f:
    json.dump(triples, f,indent=4, sort_keys=True)