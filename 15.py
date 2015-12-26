import re
from operator import mul, add
from functools import reduce

matcher = re.compile(r"\w+: \w+ (-?\d+), \w+ (-?\d+), \w+ (-?\d+), \w+ (-?\d+)")

def parse(line):
    c, d, f, t = matcher.match(line).groups()
    return tuple(map(int, (c, d, f, t)))


def calc(ingredients, max_scoop=100, acc_score=(0, 0, 0, 0)):
    if not ingredients:
        return [acc_score]

    ing, rest_ings = ingredients[0], ingredients[1:]

    scores = []
    for scoop in range(max_scoop + 1):
        ing_score = tuple(scoop * n for n in ing)
        new_acc_score = tuple(a + i for a, i in zip(ing_score, acc_score))
        rest_scores = calc(rest_ings, max_scoop - scoop, new_acc_score)
        for s in rest_scores:
            scores.append(s)

    return scores


inp = """
Sugar: capacity 3, durability 0, flavor 0, texture -3, calories 2
Sprinkles: capacity -3, durability 3, flavor 0, texture 0, calories 9
Candy: capacity -1, durability 0, flavor 4, texture 0, calories 1
Chocolate: capacity 0, durability 0, flavor -2, texture 2, calories 8
"""


lines = [l for l in inp.splitlines() if l]

ingredients = [parse(line) for line in lines]

combinations = calc(ingredients)
capped = [tuple(map(lambda n: max(0, n), tup)) for tup in combinations]
scores = [reduce(mul, tup) for tup in capped]
print(max(scores))
