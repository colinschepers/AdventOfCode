from typing import Tuple, Sequence, Set, Mapping

from utils import get_input

Food = Tuple[Set[str], Set[str]]


def get_foods(data: Sequence[str]) -> Sequence[Food]:
    foods = []
    for line in data:
        splt = line.split('(contains')
        ingredient = [x.strip(' ') for x in splt[0].strip(' ').split(' ')]
        allergen = [x.strip(' ') for x in splt[1].strip(' )').split(',')]
        foods.append((set(ingredient), set(allergen)))
    return foods


def get_allergens(foods: Sequence[Food]) -> Mapping[str, Set[str]]:
    allergens = {}
    for food in foods:
        for allergen in food[1]:
            allergens[allergen] = allergens.get(allergen, food[0]) & set(food[0])
    return allergens


def get_dangerous_ingredients(allergens: Mapping[str, Set[str]]) -> Sequence[str]:
    singles = []
    while len(singles) < len(allergens):
        singles = [ingred for ingreds in allergens.values() for ingred in ingreds if len(ingreds) == 1]
        for single in singles:
            for ingredients in allergens.values():
                if len(ingredients) > 1 and single in ingredients:
                    ingredients.remove(single)

    allergens = sorted(allergens.items(), key=lambda x: x[0])
    return [next(iter(a[1])) for a in allergens]


data = get_input(year=2020, day=21)
foods = get_foods(data)
allergens = get_allergens(foods)
positives = set(ingredient for ingredients in allergens.values() for ingredient in ingredients)

print(sum(ingredient not in positives for food in foods for ingredient in food[0]))
print(','.join(get_dangerous_ingredients(allergens)))
