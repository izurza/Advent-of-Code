input = open("inputs/day1.in", "r")
calories = input.read().split("\n\n")
for e in calories:
    t = (e.split())
    for x in t:
        t[t.index(x)]=int(x)
    calories[calories.index(e)]=sum(t)
print(max(calories))
print(sum(sorted(calories, reverse=True)[:3]))