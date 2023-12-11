# input = open("day6/inputtest.txt", "r")
input = open("day6/input.txt", "r")
b = input.read().strip() 

firstS, firstM=False,False
for i in range(len(b)):
    if not firstS and i>3 and len(set([b[i-x] for x in range(4)]))==4:
            print(i+1)
            firstS=True
    if not firstM and i>14 and len(set([b[i-x] for x in range(14)]))==14:
            print(i+1)
            firstM=True

    
