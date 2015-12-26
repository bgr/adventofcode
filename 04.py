from hashlib import md5

inp = "iwrupvqb"

n = 0

while True:
    n += 1

    concatenated = inp + str(n)

    binp = bytes(concatenated, encoding="ascii")
    md5hash = md5(binp).hexdigest()

    if md5hash.startswith("00000"):
        print(n)
        break
