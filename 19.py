import re

inp = """
Al => ThF
Al => ThRnFAr
B => BCa
B => TiB
B => TiRnFAr
Ca => CaCa
Ca => PB
Ca => PRnFAr
Ca => SiRnFYFAr
Ca => SiRnMgAr
Ca => SiTh
F => CaF
F => PMg
F => SiAl
H => CRnAlAr
H => CRnFYFYFAr
H => CRnFYMgAr
H => CRnMgYFAr
H => HCa
H => NRnFYFAr
H => NRnMgAr
H => NTh
H => OB
H => ORnFAr
Mg => BF
Mg => TiMg
N => CRnFAr
N => HSi
O => CRnFYFAr
O => CRnMgAr
O => HP
O => NRnFAr
O => OTi
P => CaP
P => PTi
P => SiRnFAr
Si => CaSi
Th => ThCa
Ti => BP
Ti => TiTi
e => HF
e => NAl
e => OMg

CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF
"""

lines = [line for line in inp.splitlines() if line]

rules = [line.split(" => ") for line in lines[:-1]]
inp_start = lines[-1]


def regexify_rules(rules):
    return [(re.compile(k), v) for k, v in rules]


def replacements_for_rule(s, rule_tup):
    rule_re, rule_to = rule_tup
    matches = rule_re.finditer(s)
    return [s[:m.start()] + rule_to + s[m.end():] for m in matches]


def replacements(s, rules_re):
    return {rep for rule in rules_re for rep in replacements_for_rule(s, rule)}


reps = replacements(inp_start, regexify_rules(rules))
print(len(reps))


# part 2

# solution is not 100% correct since it returns as soon as it finds first
# value, where in general there might be smaller values

found_depth = 0


def dig_in(s, rules_re, depth=1):
    global found_depth
    for rep in replacements(s, rules_re):
        if rep == 'e':
            found_depth = depth
        elif 'e' not in rep and not found_depth:
            dig_in(rep, rules_re, depth + 1)
        # molecules containing e and other molecules can be skipped,
        # as they can't be further reduced to just e

reverse_rules = regexify_rules([(b, a) for a, b in rules])
dig_in(inp_start, regexify_rules(reverse_rules))
print(found_depth)

# abandoned second attempt, since it consumes all memory :)
#while dq:
#    depth += 1
#    popped = dq.popleft()
#    reps = replacements(popped, reverse_rules)
#    if any(rep == 'e' for rep in reps):
#        print(depth)
#        break
#    # molecules containing e and other molecules can be skipped,
#    # as they can't be further reduced to just e
#    dq.extend([rep for rep in reps if 'e' not in rep])
