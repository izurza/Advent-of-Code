from collections import defaultdict
r1 = 0
r2 = 0
nums = defaultdict(list)
with open('2023/inputs/day3.in', 'r') as f:
    lines = f.read().strip().split('\n')
    grid = [[c for c in line] for line in lines]
    rowLength = len(grid)
    colLength = len(grid[0])

    for rowPos in range(rowLength):
        has_part = False
        n = 0
        gears = set()
        for colPos in range(colLength+1):
            if colPos<colLength and grid[rowPos][colPos].isdigit():
                n=n*10 + int(grid[rowPos][colPos])
                for rowAdy in [-1,0,1]:
                    for colAdy in [-1,0,1]:
                        if 0<=rowPos+rowAdy<rowLength and 0<=colPos+colAdy<colLength:
                            char = grid[rowPos+rowAdy][colPos+colAdy]
                            if not char.isdigit() and char != '.':
                                has_part = True
                            if char =='*':
                                gears.add((rowPos+rowAdy, colPos+colAdy))
            elif n>0:
                if has_part:
                    r1 += n
                for gear in gears:
                    nums[gear].append(n)
                n=0
                has_part = False
                gears = set()
    print(r1)
    for k,v in nums.items():
        if len(v)==2:
            r2+= v[0]*v[1]
    print(r2)
