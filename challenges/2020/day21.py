
path = './data/day21.txt'
with open(path, encoding = 'utf-8') as f:
    lines = [l.strip() for l in f.readlines()]
 
foods = []
for line in lines:
    splt = line.split('(contains')
    ingred = [x.strip(' ') for x in splt[0].strip(' ').split(' ')]
    allergen = [x.strip(' ') for x in splt[1].strip(' )').split(',')]
    foods.append((set(ingred), set(allergen)))

allergens = {}
for food in foods:
    for allergen in food[1]:
        allergens[allergen] = allergens.get(allergen, food[0]) & set(food[0])

positives = set(ingred for ingreds in allergens.values() for ingred in ingreds)
solution = sum(ingred not in positives for food in foods for ingred in food[0])

print(solution)


singles = []
while len(singles) < len(allergens):
    singles = [ingred for ingreds in allergens.values() for ingred in ingreds if len(ingreds) == 1]
    for single in singles:
        for ingreds in allergens.values():
            if len(ingreds) > 1 and single in ingreds:
                ingreds.remove(single)

allergens = sorted(allergens.items(), key=lambda x: x[0])
allergens = [next(iter(a[1])) for a in allergens]
dangerous = ','.join(allergens)

print(dangerous)