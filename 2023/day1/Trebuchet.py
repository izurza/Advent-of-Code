r1=0
r2=0
with open('2023/inputs/day1.in', 'r') as f:
    lines = f.read().strip().split('\n')
    for l in lines:
        p1 =[]
        p2 =[]
        for i, c in enumerate(l):
            if c.isdigit(): 
                p1.append(c)
                p2.append(c)
            for j,w in enumerate(['one','two','three','four','five','six','seven','eight','nine']):
                if l[i:].startswith(w):
                    p2.append(str(j+1))
        r1 += int(p1[0]+p1[-1])
        r2 += int(p2[0]+p2[-1])
print(r1)       
print(r2)
            
