inp_liters = 150

inp = """
33
14
18
20
45
35
16
35
1
13
18
13
50
44
48
6
24
41
30
42
"""


from itertools import combinations

sizes = [int(l) for l in inp.splitlines() if l]

all_combs = [c for n in range(len(sizes)) for c in combinations(sizes, n)]

matching_combs = [c for c in all_combs if sum(c) == inp_liters]

print(len(matching_combs))

# part 2

comb_lengths = [len(c) for c in matching_combs]
minimal_length = min(sorted(comb_lengths))
print(len([0 for cl in comb_lengths if cl == minimal_length]))
