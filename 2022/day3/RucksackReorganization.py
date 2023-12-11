input = open("inputs/day3.in", "r")

r = input.read().split('\n')
repeated=False

# print(ord("a")-96)
# print(ord("A")-38)

prio=[]
for i in r:
    fh=i[:len(i)//2]
    sh=i[len(i)//2:]
    #print(fh," ", sh)
    for l in fh:
        for l2 in sh:
            if repeated: continue
            if l==l2:
                repeated=True
                if (l.islower()):
                    prio.append(ord(l)-96)
                else:
                    prio.append(ord(l)-38)
    repeated=False
print(sum(prio))

prio.clear()
for e in range(len(r)):
    if(e%3==2):
        for i in r[e]:
            for i2 in r[e-1]:
                for i3 in r[e-2]:
                    if repeated:continue
                    if i==i2==i3:
                        repeated=True
                        if (i.islower()):
                            prio.append(ord(i)-96)
                        else:
                            prio.append(ord(i)-38)
        repeated=False
print(sum(prio))