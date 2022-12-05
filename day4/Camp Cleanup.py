# input = open("day4/inputtest.txt", "r")
input = open("day4/input.txt", "r")
eh = input.read().split('\n')
overlap1=0
overlap2=0
for ep in eh:
    e1=ep.split(",")[0]
    e2=ep.split(",")[1]

    ze1=set([z for z in range(int(e1.split("-")[0]),int(e1.split("-")[1])+1)])
    ze2=set([z for z in range(int(e2.split("-")[0]),int(e2.split("-")[1])+1)])
    if (ze1.issubset(ze2)  or ze2.issubset(ze1)): 
        overlap1+=1
    if len(ze1.intersection(ze2))>=1:
        overlap2+=1
    
print(overlap1,"\n",overlap2)