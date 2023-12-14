from collections import defaultdict
r1=0
r2=0

with open('2023/inputs/day4.in', 'r') as f:
    lines = f.read().strip().split('\n')
    copies = defaultdict(int)
    for l in lines:
        cn,l = l.split(':')
        cn=int(cn.split()[1])
        copies[cn] += 1 
        W, N = l.split('|')
        W = W.split()
        N = N.split()
        first=True
        points=0
        i=0
        for n in N:
            if n in W:
                i+=1
                for r in range(copies[cn]):
                    copies[cn+i] += 1   
                if first:
                    points=1
                    first = False
                else:
                    points*=2
        r1 += points
    for sc in copies.items():
        r2 += sc[1]
print(r1)
print(r2)