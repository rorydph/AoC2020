with open("1-input.txt") as f:
    entries = [int(x) for x in f.read().split()]
for x in entries:
    for y in entries[1:]:
        for z in entries[2:]:
            if x + y + z == 2020:
                product = x * y * z
print(product)
