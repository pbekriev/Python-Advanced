letters = {}

for leter in input():
    if leter not in letters:
        letters[leter] = 0
    letters[leter] += 1

for k, v in sorted(letters.items()):
    print(f"{k}: {v} time/s")
