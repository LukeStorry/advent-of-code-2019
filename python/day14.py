import re

reactions = open('../input/14.txt').read().split('\n')
recipes = {output[1]: (output[0], ingredients) for *ingredients, output in
           [[(int(x), y) for x, y in re.findall(r'([0-9]+) ([A-Z]+)', reaction)]
            for reaction in reactions]}

requirements = {'ORE': 0, 'FUEL': 1}
while True:
    remaining = [r for r in requirements if r != 'ORE' and requirements[r] > 0]
    if not remaining:
        break

    for chemical in remaining:
        (output_quantity, recipe) = recipes[chemical]

        for (quantity, ingredient) in recipe:
            requirements[ingredient] = requirements.get(ingredient, 0) + quantity

        requirements[chemical] -= output_quantity

print(requirements['ORE'])
