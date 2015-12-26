from collections import defaultdict
from itertools import permutations
from functools import reduce
import re

matcher = re.compile(r"(\w+) \w+ (\w+) (\d+) \w+ \w+ \w+ \w+ \w+ \w+ (\w+)")

def write_unit(line, d):
    m = matcher.match(line)
    person_a, person_b = m.group(1), m.group(4)
    multiplier = -1 if m.group(2) == 'lose' else 1
    amount = int(m.group(3)) * multiplier
    units[person_a][person_b] = amount


def get_dist(persons, units):
    def reducer(tup, next_person):
        cur_person, acc_dist = tup
        units_ab = units[cur_person][next_person]
        units_ba = units[next_person][cur_person]
        return (next_person, acc_dist + units_ab + units_ba)
    first, last = persons[0], persons[-1]
    initial = units[first][last] + units[last][first]
    _, dist = reduce(reducer, persons[1:], (persons[0], initial))
    return dist


inp = r"""
Alice would lose 57 happiness units by sitting next to Bob.
Alice would lose 62 happiness units by sitting next to Carol.
Alice would lose 75 happiness units by sitting next to David.
Alice would gain 71 happiness units by sitting next to Eric.
Alice would lose 22 happiness units by sitting next to Frank.
Alice would lose 23 happiness units by sitting next to George.
Alice would lose 76 happiness units by sitting next to Mallory.
Bob would lose 14 happiness units by sitting next to Alice.
Bob would gain 48 happiness units by sitting next to Carol.
Bob would gain 89 happiness units by sitting next to David.
Bob would gain 86 happiness units by sitting next to Eric.
Bob would lose 2 happiness units by sitting next to Frank.
Bob would gain 27 happiness units by sitting next to George.
Bob would gain 19 happiness units by sitting next to Mallory.
Carol would gain 37 happiness units by sitting next to Alice.
Carol would gain 45 happiness units by sitting next to Bob.
Carol would gain 24 happiness units by sitting next to David.
Carol would gain 5 happiness units by sitting next to Eric.
Carol would lose 68 happiness units by sitting next to Frank.
Carol would lose 25 happiness units by sitting next to George.
Carol would gain 30 happiness units by sitting next to Mallory.
David would lose 51 happiness units by sitting next to Alice.
David would gain 34 happiness units by sitting next to Bob.
David would gain 99 happiness units by sitting next to Carol.
David would gain 91 happiness units by sitting next to Eric.
David would lose 38 happiness units by sitting next to Frank.
David would gain 60 happiness units by sitting next to George.
David would lose 63 happiness units by sitting next to Mallory.
Eric would gain 23 happiness units by sitting next to Alice.
Eric would lose 69 happiness units by sitting next to Bob.
Eric would lose 33 happiness units by sitting next to Carol.
Eric would lose 47 happiness units by sitting next to David.
Eric would gain 75 happiness units by sitting next to Frank.
Eric would gain 82 happiness units by sitting next to George.
Eric would gain 13 happiness units by sitting next to Mallory.
Frank would gain 77 happiness units by sitting next to Alice.
Frank would gain 27 happiness units by sitting next to Bob.
Frank would lose 87 happiness units by sitting next to Carol.
Frank would gain 74 happiness units by sitting next to David.
Frank would lose 41 happiness units by sitting next to Eric.
Frank would lose 99 happiness units by sitting next to George.
Frank would gain 26 happiness units by sitting next to Mallory.
George would lose 63 happiness units by sitting next to Alice.
George would lose 51 happiness units by sitting next to Bob.
George would lose 60 happiness units by sitting next to Carol.
George would gain 30 happiness units by sitting next to David.
George would lose 100 happiness units by sitting next to Eric.
George would lose 63 happiness units by sitting next to Frank.
George would gain 57 happiness units by sitting next to Mallory.
Mallory would lose 71 happiness units by sitting next to Alice.
Mallory would lose 28 happiness units by sitting next to Bob.
Mallory would lose 10 happiness units by sitting next to Carol.
Mallory would gain 44 happiness units by sitting next to David.
Mallory would gain 22 happiness units by sitting next to Eric.
Mallory would gain 79 happiness units by sitting next to Frank.
Mallory would lose 16 happiness units by sitting next to George.
"""

units = defaultdict(dict)

lines = [l for l in inp.splitlines() if l]

for line in lines:
    write_unit(line, units)

def print_result():
    perms = list(permutations(units.keys()))
    all_units = [get_dist(perm, units) for perm in perms]
    print(max(all_units))

print_result()

# part 2

def add_me(name):
    units['Me'][name] = 0
    units[name]['Me'] = 0

names = list(units.keys())
[add_me(n) for n in names]

print_result()
