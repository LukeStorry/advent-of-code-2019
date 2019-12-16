import re

reactions = open('../input/14.txt').read().split('\n')
recipes = {output[1]: (output[0], ingredients) for *ingredients, output in
           [[(int(x), y) for x, y in re.findall(r'([0-9]+) ([A-Z]+)', reaction)]
            for reaction in reactions]}
stock = {ingredient: 0 for ingredient in recipes}

print(recipes)
print(stock)
