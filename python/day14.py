import re

recipes = {output_chemical: (output_quantity, recipe) for *recipe, (output_quantity, output_chemical) in
           [[(int(x), y) for x, y in re.findall(r'([0-9]+) ([A-Z]+)', reaction)]
            for reaction in (open('../input/14.txt').read().split('\n'))]}


def calc_ore_for(fuel_amount):
    requirements = {'FUEL': fuel_amount}
    while True:
        remaining = [r for r in requirements if r != 'ORE' and requirements[r] > 0]
        if not remaining:
            break

        for chemical in remaining:
            (output_quantity, recipe) = recipes[chemical]
            repeats = (requirements[chemical] + output_quantity - 1) // output_quantity

            for (quantity, ingredient) in recipe:
                requirements[ingredient] = requirements.get(ingredient, 0) + quantity * repeats

            requirements[chemical] -= output_quantity * repeats

    return requirements['ORE']


print(calc_ore_for(1))

ore_available = 1000000000000
lower_bound = 1
upper_bound = 10

while calc_ore_for(upper_bound) <= ore_available:
    lower_bound *= 10
    upper_bound *= 10

while upper_bound > lower_bound + 1:
    center = (upper_bound + lower_bound) // 2
    if calc_ore_for(center) > ore_available:
        upper_bound = center
    else:
        lower_bound = center

print(lower_bound)
