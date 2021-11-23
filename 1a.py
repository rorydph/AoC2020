with open("1-input.txt") as f:
    entries = [int(x) for x in f.read().split()]
for x in entries:
    for y in entries:
        if x + y == 2020 and x != y:
            print(x * y)
            break
#print(product)
