from collections import defaultdict
import re

matcher = re.compile(r"(\w+) \w+ \w+ (\d+) km/s for (\d+) \w+, \w+ \w+ \w+ \w+ \w+ (\d+)")

def write_unit(line, d):
    m = matcher.match(line)
    name, speed, lasts, rests = m.groups()
    d[name] = tuple(map(int, (speed, lasts, rests)))


def calc(duration, speed, lasts, rests):
    whole_chunks, remain_seconds = divmod(duration, lasts + rests)
    whole_sums = whole_chunks * (speed * lasts)
    last_chunk = min(remain_seconds, lasts) * speed
    return whole_sums + last_chunk


def get_leads(at_second, units):
    speeds = { name: calc(at_second, *vals) for name, vals in units.items() }
    max_speed = max(speeds.values())
    return [name for name, speed in speeds.items() if speed == max_speed]


def calc_new_score(duration, units):
    scores = defaultdict(int)
    for second in range(1, duration + 1):
        for name in get_leads(second, units):
            scores[name] += 1
    return max(scores.values())

inp_dur = 2503

inp = """
Vixen can fly 8 km/s for 8 seconds, but then must rest for 53 seconds.
Blitzen can fly 13 km/s for 4 seconds, but then must rest for 49 seconds.
Rudolph can fly 20 km/s for 7 seconds, but then must rest for 132 seconds.
Cupid can fly 12 km/s for 4 seconds, but then must rest for 43 seconds.
Donner can fly 9 km/s for 5 seconds, but then must rest for 38 seconds.
Dasher can fly 10 km/s for 4 seconds, but then must rest for 37 seconds.
Comet can fly 3 km/s for 37 seconds, but then must rest for 76 seconds.
Prancer can fly 9 km/s for 12 seconds, but then must rest for 97 seconds.
Dancer can fly 37 km/s for 1 seconds, but then must rest for 36 seconds.
"""


lines = [l for l in inp.splitlines() if l]
units = {}

for line in lines:
    write_unit(line, units)

print(calc_new_score(inp_dur, units))
