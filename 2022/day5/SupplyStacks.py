input = open("inputs/day5.in", "r")
stateandmoving = input.read().split('\n\n')


#process the initial data of boxes position
state = stateandmoving[0]
stackN=state.split("\n")[-1].split()
boxesofeachlevel = state.split("\n")[0:-1]
stackPiles={}
column =1
for x in boxesofeachlevel:
    for n in x[1::4]:
        if column in stackPiles:
            temp= stackPiles[column]
            temp.append(n)
            stackPiles[column]=temp
        else:
            if n!=" ":
                stackPiles[column]=[n]
        column+=1
    column=1

for x in stackPiles.values():
    x.reverse()
# to be more elegant
stackPiles=dict(sorted(stackPiles.items()))

#Process all the moving strategy
moving = stateandmoving[1].split("\n")
for m in moving:
    move = m.split(" ")
    cuantity = int(move[1]) #get the cuantity of boxes to move
    start = int(move[3]) #get the starting column 
    finish = int(move[5]) #get the ending column

    temp=[]
    #try with .pop()
    for x in range(cuantity, 0,-1):
        temp.append(stackPiles.get(start)[-x])
        del stackPiles.get(start)[-x]
        
        
#for part one 
    # for b in reversed(temp):
    #     stackPiles.get(finish).append(b)
#for part two
    for b in temp:
        stackPiles.get(finish).append(b)


for x in stackPiles.values():
    print(x[-1],end="")