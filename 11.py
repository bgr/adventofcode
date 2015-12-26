from string import ascii_lowercase as alphabet
import re

re_pairs = re.compile(r".*?(.)\1.*?(.)\2")


def next_char(c):
    """ Returns tuple (char, carry_bool)."""
    if c == 'z':
        return ('a', True)
    else:
        return (chr(ord(c) + 1), False)

def increment(s):
    if not s:
        return ''

    new_last_char, carry = next_char(s[-1])
    if carry:
        return increment(s[:-1]) + new_last_char
    else:
        return s[:-1] + new_last_char


# a bit of ad-hoc TDD
assert increment('a') == 'b'
assert increment('y') == 'z'
assert increment('kz') == 'la'
assert increment('bkzzz') == 'blaaa'



triplets = [''.join(tup) for tup in zip(alphabet, alphabet[1:], alphabet[2:])]

def has_straight_triplet(s):
    return any(tri in s for tri in triplets)

def no_iol(s):
    return all(not ch in s for ch in "iol")

def has_two_pairs(s):
    match = re_pairs.match(s)
    if not match:
        return False
    return match.group(1) != match.group(2)


def password_ok(pw):
    return has_straight_triplet(pw) and no_iol(pw) and has_two_pairs(pw)


assert has_straight_triplet("hijklmmn")
assert not password_ok("hijklmmn")

assert has_two_pairs("abbceffg")
assert not password_ok("abbceffg")

assert has_two_pairs("bbzaa")
assert not has_two_pairs("aazaa")

assert password_ok("abcdffaa")
assert password_ok("ghjaabcc")


def get_next_password(cur_password):
    while True:
        cur_password = increment(cur_password)
        if password_ok(cur_password):
            return cur_password


assert get_next_password("abcdefgh") == "abcdffaa"
# this takes long
# assert get_next_password("ghijklmn") == "ghjaabcc"
# print("all ok")


inp = "cqjxjnds"

part_1 = get_next_password(inp)
part_2 = get_next_password(part_1)

print(part_1)
print(part_2)
