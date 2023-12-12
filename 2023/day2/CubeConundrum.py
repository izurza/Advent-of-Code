from collections import defaultdict
reds = 12
greens = 13
blues = 14
r1 = 0
r2 = 0
with open('2023/inputs/day2.in', 'r') as f:
    lines = f.read().strip().split('\n')
    for l in lines:
        impossible = False
        game, sets =l.split(':')
        game = int(game.split()[-1])
        minimumCubes = defaultdict(int)
        for s in sets.split(';'):
            for c in s.split(','):
                n,color = c.strip().split(' ')
                n= int(n)
                minimumCubes[color]=max(minimumCubes[color],n)
                if color.startswith('red') and n>reds:
                    impossible = True
                if color.startswith('blue') and n>blues:
                    impossible = True
                if color.startswith('green') and n>greens:
                    impossible = True
        if not impossible:
            r1+= game
        power = 1
        for mc in minimumCubes.values():
            power *= mc
        r2 += power

print(r1)
print(r2)
