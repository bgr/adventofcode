from itertools import groupby

def look_and_say(s):
    return ''.join(str(len(list(group))) + elem for elem, group in groupby(s))


inp = "1113222113"

for i in range(40):
    inp = look_and_say(inp)

print(len(inp))
