input = open("day2/input.txt", "r")
#A Rock
#B Paper
#C Scissors

case1,case2=[],[]
# Case 1
# X = Rock
# Y = Paper
# Z = Scissors

# Case 2 
# X = Lose
# Y = Draw
# Z = Win

s = input.read().split('\n')

for p in s:
    if ((p.split()[0] == "A") & (p.split()[1]=="X")):
        case1.append(1+3)#Rock=Draw
        case2.append(0+3)#Lose=Scissors
    elif ((p.split()[0] == "A") & (p.split()[1]=="Y")):
        case1.append(2+6)#Paper=Win
        case2.append(3+1)#Draw=Rock
    elif ((p.split()[0] == "A") & (p.split()[1]=="Z")):
        case1.append(3+0)#Scissors=Lose
        case2.append(6+2)#Win=Paper
    ############################################
    if ((p.split()[0] == "B") & (p.split()[1]=="X")):
        case1.append(1+0)#Rock=Lose
        case2.append(0+1)#Lose=Rock
    elif ((p.split()[0] == "B") & (p.split()[1]=="Y")):
        case1.append(2+3)#Paper=Draw
        case2.append(3+2)#Draw=Paper
    elif ((p.split()[0] == "B") & (p.split()[1]=="Z")):
        case1.append(3+6)#Scissor=Win
        case2.append(6+3)#Win=Scissors
    ############################################
    if ((p.split()[0] == "C") & (p.split()[1]=="X")):
        case1.append(1+6)#Rock=Win
        case2.append(0+2)#Lose=Paper
    elif ((p.split()[0] == "C") & (p.split()[1]=="Y")):
        case1.append(2+0)#Paper=Lose
        case2.append(3+3)#Draw=Scissors
    elif ((p.split()[0] == "C") & (p.split()[1]=="Z")):
        case1.append(3+3)#Scissors=Draw
        case2.append(6+1)#Win=Rock

print("strategy 1:", sum(case1))
print("strategy 2:", sum(case2))
