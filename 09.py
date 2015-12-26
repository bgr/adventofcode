from collections import defaultdict
from itertools import permutations
from functools import reduce

dists = defaultdict(dict)


def write_dist(line):
    cities, _, dist = line.partition(' = ')
    city_a, _, city_b = cities.partition(' to ')
    dists[city_a][city_b] = int(dist)
    dists[city_b][city_a] = int(dist)


def get_dist(cities, dists):
    def reducer(tup, next_city):
        cur_city, acc_dist = tup
        return (next_city, acc_dist + dists[cur_city][next_city])
    _, dist = reduce(reducer, cities[1:], (cities[0], 0))
    return dist


inp = r"""
Faerun to Tristram = 65
Faerun to Tambi = 129
Faerun to Norrath = 144
Faerun to Snowdin = 71
Faerun to Straylight = 137
Faerun to AlphaCentauri = 3
Faerun to Arbre = 149
Tristram to Tambi = 63
Tristram to Norrath = 4
Tristram to Snowdin = 105
Tristram to Straylight = 125
Tristram to AlphaCentauri = 55
Tristram to Arbre = 14
Tambi to Norrath = 68
Tambi to Snowdin = 52
Tambi to Straylight = 65
Tambi to AlphaCentauri = 22
Tambi to Arbre = 143
Norrath to Snowdin = 8
Norrath to Straylight = 23
Norrath to AlphaCentauri = 136
Norrath to Arbre = 115
Snowdin to Straylight = 101
Snowdin to AlphaCentauri = 84
Snowdin to Arbre = 96
Straylight to AlphaCentauri = 107
Straylight to Arbre = 14
AlphaCentauri to Arbre = 46
"""

lines = [l for l in inp.splitlines() if l]

for line in lines:
    write_dist(line)

perms = list(permutations(dists.keys()))

all_dists = [get_dist(perm, dists) for perm in perms]
print("min: {}".format(min(all_dists)))
print("max: {}".format(max(all_dists)))
