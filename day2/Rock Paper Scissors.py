input = open("day2/input.txt", "r")
#A Rock
#B Paper
#C Scissors

one = {'X':'A','Y':'B','Z':'C'} # X es piedra 1, Y es Papel 2 Z es tijeras 3
two = {'X':'A','Y':'C','Z':'B'} # X es piedra 1, Y es tijeras 3 Z es papel 2
three = {'X':'B','Y':'A','Z':'C'} # X es papel 2, Y es piedra 1 Z es tijeras 3
four = {'X':'B','Y':'C','Z':'A'} # X es papel 2, Y es tijeras 3 Z es piedra 1
five = {'X':'C','Y':'A','Z':'B'} # X es tijeras 3, Y es Piedra 1 Z es papel 2
six = {'X':'C','Y':'B','Z':'A'} # X es tijeras 3, Y es Papel 2 Z es piedra 1
case1,case2,case3,case4,case5,case6=[],[],[],[],[],[]
s = input.read().split('\n')

for p in s:
    if ((p.split()[0] == "A") & (p.split()[1]=="X")):
        case1.append(1+3)#piedra + empate
        case2.append(1+3)#piedra + empate
        case3.append(2+6)#papel + ganar
        case4.append(2+6)#papel + ganar
        case5.append(3+0)#tijeras + perder
        case6.append(3+0)#tijeras + perder
    elif ((p.split()[0] == "A") & (p.split()[1]=="Y")):
        case1.append(2+6)#papel + ganar
        case2.append(3+0)#tijeras + perder
        case3.append(1+3)#piedra + empate
        case4.append(3+0)#tijeras + perder
        case5.append(1+3)#piedra + empate
        case6.append(2+6)#papel + ganar
    elif ((p.split()[0] == "A") & (p.split()[1]=="Z")):
        case1.append(3+0)#tijeras + perder
        case2.append(2+6)#papel + ganar
        case3.append(3+0)#tijeras + perder
        case4.append(1+3)#piedra + empate
        case5.append(2+6)#papel + ganar
        case6.append(1+3)#piedra + empate
    ############################################
    if ((p.split()[0] == "B") & (p.split()[1]=="X")):
        case1.append(1+0)#piedra + perder
        case2.append(1+0)#piedra + perder
        case3.append(2+3)#papel + empate
        case4.append(2+3)#papel + empate
        case5.append(3+6)#tijeras + ganar
        case6.append(3+6)#tijeras + ganar
    elif ((p.split()[0] == "B") & (p.split()[1]=="Y")):
        case1.append(2+3)#papel + empate
        case2.append(3+6)#tijeras + ganar
        case3.append(1+0)#piedra + perder
        case4.append(3+6)#tijeras + ganar
        case5.append(1+0)#piedra + perder
        case6.append(2+3)#papel + empate
    elif ((p.split()[0] == "B") & (p.split()[1]=="Z")):
        case1.append(3+6)#tijeras + ganar
        case2.append(2+3)#papel + empate
        case3.append(3+6)#tijeras + ganar
        case4.append(1+0)#piedra + perder
        case5.append(2+3)#papel + empate
        case6.append(1+0)#piedra + perder
    ############################################
    if ((p.split()[0] == "C") & (p.split()[1]=="X")):
        case1.append(1+6)#piedra + ganar
        case2.append(1+6)#piedra + ganar
        case3.append(2+0)#papel + perder
        case4.append(2+0)#papel + perder
        case5.append(3+3)#tijeras + empate
        case6.append(3+3)#tijeras + empate
    elif ((p.split()[0] == "C") & (p.split()[1]=="Y")):
        case1.append(2+0)#papel + perder
        case2.append(3+3)#tijeras + empate
        case3.append(1+6)#piedra + ganar
        case4.append(3+3)#tijeras + empate
        case5.append(1+6)#piedra + ganar
        case6.append(2+0)#papel + perder
    elif ((p.split()[0] == "C") & (p.split()[1]=="Z")):
        case1.append(3+3)#tijeras + empate
        case2.append(2+0)#papel + perder
        case3.append(3+3)#tijeras + empate
        case4.append(1+6)#piedra + ganar
        case5.append(2+0)#papel + perder
        case6.append(1+6)#piedra + ganar

print("strategy 1**:", sum(case1))
print("strategy 2:", sum(case2))
print("strategy 3:", sum(case3))
print("strategy 4:", sum(case4))
print("strategy 5:", sum(case5))
print("strategy 6:", sum(case6))