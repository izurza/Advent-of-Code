from collections import defaultdict

#learned from Jonathan Paulson

input = open("inputs/day7.in", "r")
cl = input.read().split("\n")
SZ=defaultdict(int)
path=[]
for l in cl:
    words = l.strip().split()
    if words[1]=="cd":#moving
        if words[2]=="..": #parent folder
            path.pop()
        else : 
            path.append(words[2]) #next folder
    elif words[1]=="ls": #do nothing
        continue
    elif words[0]=="dir": #do nothing
        continue
    else: #get the value of the files and sum them to the path
        sz=int(words[0])
        for i in range(len(path)+1):
            SZ['/'.join(path[:i])]+=sz

#conditions for part 2
max_used =70000000-30000000
total_used = SZ['/']
need_to_free = total_used - max_used
best = 1e9

ans=0
for k,v in SZ.items():
    print(k)
    if v<=100000:#get the values of the directories that have size no more than 100000
        ans+=v 
    if v>=need_to_free: #get the value of the directory with the minimum size, that lets you update
        best=min(best,v)
print(ans)
print(best)